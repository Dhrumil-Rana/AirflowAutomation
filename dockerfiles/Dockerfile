FROM puckel/docker-airflow:1.10.9

RUN pwd
COPY . /usr/local/airflow
COPY ./requirements.txt /usr/local/airflow
RUN ls
RUN pip install -r requirements.txt
#ENTRYPOINT ["python", "dags/dag_example.py" ]