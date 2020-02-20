# How to hyperparameter tuning using hyperopt

The original inspiration came from [here](https://docs.azuredatabricks.net/_static/notebooks/hyperopt-sklearn-model-selection.html).


Please check [Hyperparatemer tuning](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)) for more details on the basic principles.


`hyperopt` is one of the many open source libraries available to do it in Python. Here is an example on how to use it to optimize the type classifier and its parameters at the end of sklearn pipeline


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

     25%|██▌       | 1/4 [00:00<00:01,  2.65it/s, best loss: -0.933]

    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/sklearn/neural_network/multilayer_perceptron.py:566: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
      % self.max_iter, ConvergenceWarning)
    


    100%|██████████| 4/4 [00:07<00:00,  1.86s/it, best loss: -0.944]

