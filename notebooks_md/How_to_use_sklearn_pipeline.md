# How to use sklearn Pipeline

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


