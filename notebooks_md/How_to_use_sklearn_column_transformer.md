# How to use sklearn column transformer


```python
from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier

data = make_classification(1000)

pipe = make_pipeline(
    ColumnTransformer(
        [
            ("scaled", StandardScaler(), slice(0, 10)),
            ("disc", KBinsDiscretizer(n_bins=10), slice(10,12)),
            ("rest", "passthrough", slice(12,20))
    ]), 
    PCA(n_components=2),
    MLPClassifier()
)

pipe.fit(*data)

```




    Pipeline(memory=None,
             steps=[('columntransformer',
                     ColumnTransformer(n_jobs=None, remainder='drop',
                                       sparse_threshold=0.3,
                                       transformer_weights=None,
                                       transformers=[('scaled',
                                                      StandardScaler(copy=True,
                                                                     with_mean=True,
                                                                     with_std=True),
                                                      slice(0, 10, None)),
                                                     ('disc',
                                                      KBinsDiscretizer(encode='onehot',
                                                                       n_bins=10,
                                                                       strategy='quantile'),
                                                      slice(10, 12, None)),
                                                     ('rest', 'passthrough...
                                   batch_size='auto', beta_1=0.9, beta_2=0.999,
                                   early_stopping=False, epsilon=1e-08,
                                   hidden_layer_sizes=(100,),
                                   learning_rate='constant',
                                   learning_rate_init=0.001, max_iter=200,
                                   momentum=0.9, n_iter_no_change=10,
                                   nesterovs_momentum=True, power_t=0.5,
                                   random_state=None, shuffle=True, solver='adam',
                                   tol=0.0001, validation_fraction=0.1,
                                   verbose=False, warm_start=False))],
             verbose=False)


