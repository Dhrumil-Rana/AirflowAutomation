from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

def print_hello(*args, **kwargs):
    return 'Hello world from {}'.format(kwargs['name'])

with DAG (dag_id="dag_example", schedule_interval="@daily",
          default_args={"owner":"airflow", "retries":1, "retry_delay":timedelta(minutes=5),"start_date":datetime(2025,1,1)},
         catchup=False) as d:
    task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
        op_kwargs={"name":"Dhrumil"}
    )

