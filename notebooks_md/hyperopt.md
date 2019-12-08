# hyperopt

[Source](https://docs.azuredatabricks.net/_static/notebooks/hyperopt-sklearn-model-selection.html)


[Hyperparatemer](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)) tuning is a hot topic right now.

`hyperopt` is one o fthe library used to make it feasible.

Here is an example on how to use it to optimize the type classifier and its parameters at the end of sklearn pipeline


```python
from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from hyperopt import tpe, hp, fmin, STATUS_OK

x, y = make_classification(1000)

def objective(params):
    global x, y
    pipe = make_pipeline(
        ColumnTransformer(
            [
                ("scaled", StandardScaler(), slice(0, 10)),
                ("disc", KBinsDiscretizer(n_bins=10), slice(10,12)),
                ("rest", "passthrough", slice(12,20))
        ]), 
        PCA(n_components=2),
        params["model"](**params["kwargs"])
    )
    
    pipe.fit(x, y)

    accuracy =accuracy_score(pipe.predict(x), y)
    
    return {'loss': -accuracy, "status": STATUS_OK}

search_space = hp.choice("classifier",[
        {'model': KNeighborsClassifier,
        'kwargs': {'n_neighbors': hp.choice('n_neighbors',range(3,11))}
        },
        {'model': MLPClassifier,
        'kwargs': {'hidden_layer_sizes':hp.choice('layers',[(10,10), (100,100), (256,256)])}}
        ])


best_result = fmin(
    fn=objective, 
    space=search_space,
    algo=tpe.suggest,
    max_evals=4,
    )

```

    100%|██████████| 4/4 [00:09<00:00,  2.35s/it, best loss: -0.932]

