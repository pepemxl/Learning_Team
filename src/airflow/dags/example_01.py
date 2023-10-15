from airflow.models import DAG
from datetime import datetime

default_arguments = {
    'owner': 'pepe',
    'email': 'pepe@localhost.com',
    'start_date': datetime(2021, 12, 5)
}


etl_dag = DAG('etl_workflow', default_args=default_arguments)