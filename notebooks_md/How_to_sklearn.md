# sklearn

## Pipeline

Useful API to chain operations on dataset.


```python
from sklearn.datasets import make_classification
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

data = make_classification(1000)

pipe = make_pipeline(
    StandardScaler(),
    PCA(),
    LogisticRegression()
)

pipe.fit(*data)

```

    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:432: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.
      FutureWarning)





    Pipeline(memory=None,
             steps=[('standardscaler',
                     StandardScaler(copy=True, with_mean=True, with_std=True)),
                    ('pca',
                     PCA(copy=True, iterated_power='auto', n_components=None,
                         random_state=None, svd_solver='auto', tol=0.0,
                         whiten=False)),
                    ('logisticregression',
                     LogisticRegression(C=1.0, class_weight=None, dual=False,
                                        fit_intercept=True, intercept_scaling=1,
                                        l1_ratio=None, max_iter=100,
                                        multi_class='warn', n_jobs=None,
                                        penalty='l2', random_state=None,
                                        solver='warn', tol=0.0001, verbose=0,
                                        warm_start=False))],
             verbose=False)



## Feature aggregation


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

    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/sklearn/neural_network/multilayer_perceptron.py:566: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
      % self.max_iter, ConvergenceWarning)





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



## Column Transformer


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

    /home/mlegoff/anaconda3/envs/juicy/lib/python3.7/site-packages/sklearn/neural_network/multilayer_perceptron.py:566: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
      % self.max_iter, ConvergenceWarning)





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


