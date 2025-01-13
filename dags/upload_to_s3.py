from datetime import timedelta
from airflow import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import boto3
import os
from pathlib import Path

# This function is used to upload the file in local to s3 bucket
def upload_to_s3():

    movies = Path("/usr/local/airflow/data/movies.csv")
    ratings = Path("/usr/local/airflow/data/ratings.csv")
    players = Path("/usr/local/airflow/data/wc2018-players.csv")
    # putting the csv files in the list
    upload_csv: list = [movies, ratings, players]
    print(upload_csv)
    # getting the bucket name and file path from the environment variable
    bucket_name = os.environ.get('BUCKET_NAME')
    file_path = os.environ.get('FILE_PATH')
    print(bucket_name)
    print(file_path)

    try:
        print("Uploading to S3")
        s3_hook = S3Hook(aws_access_key_id='',
                        aws_secret_access_key='',
                        region_name='us-east-1')
        for file in upload_csv:
            s3_hook.load_file(filename=file,key=file_path,bucket_name=bucket_name,replace=True)
            print("Upload Completed for the file: {}.formaat(file)")
        return 'Upload Completed'
    except Exception as e:
        print(e)

# Defining the default arguments
with DAG (dag_id="upload_to_s3", schedule_interval="@daily",
          default_args={"owner":"airflow", "retries":1, "retry_delay":timedelta(minutes=2),"start_date":datetime(2025,1,1)},
         catchup=False) as d:
    task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )


