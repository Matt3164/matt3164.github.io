# mlflow

[Source](https://www.mlflow.org/docs/latest/tutorial.html)


```python
"""import mlflow

with mlflow.start_run():
        
        # ... Fit model   

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(lr, "model")"""
```




    'import mlflow\n\nwith mlflow.start_run():\n        \n        # ... Fit model   \n\n        mlflow.log_param("alpha", alpha)\n        mlflow.log_param("l1_ratio", l1_ratio)\n        mlflow.log_metric("rmse", rmse)\n        mlflow.log_metric("r2", r2)\n        mlflow.log_metric("mae", mae)\n\n        mlflow.sklearn.log_model(lr, "model")'




```python
"""import mlflow

with mlflow.start_run():
        
        # ... Fit model   

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(lr, "model")"""
```




    'import mlflow\n\nwith mlflow.start_run():\n        \n        # ... Fit model   \n\n        mlflow.log_param("alpha", alpha)\n        mlflow.log_param("l1_ratio", l1_ratio)\n        mlflow.log_metric("rmse", rmse)\n        mlflow.log_metric("r2", r2)\n        mlflow.log_metric("mae", mae)\n\n        mlflow.sklearn.log_model(lr, "model")'


