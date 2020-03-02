# How to use sklearn feature aggregation


```python
from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.neural_network import MLPClassifier

data = make_classification(1000)

pipe = make_pipeline(
    StandardScaler(),
    make_union( 
                PCA(n_components=2),
                TruncatedSVD(n_components=2),
                KBinsDiscretizer()
                ),
    MLPClassifier()
)

pipe.fit(*data)
```




    Pipeline(memory=None,
             steps=[('standardscaler',
                     StandardScaler(copy=True, with_mean=True, with_std=True)),
                    ('featureunion',
                     FeatureUnion(n_jobs=None,
                                  transformer_list=[('pca',
                                                     PCA(copy=True,
                                                         iterated_power='auto',
                                                         n_components=2,
                                                         random_state=None,
                                                         svd_solver='auto', tol=0.0,
                                                         whiten=False)),
                                                    ('truncatedsvd',
                                                     TruncatedSVD(algorithm='randomized',
                                                                  n_components=2,
                                                                  n_ite...
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


