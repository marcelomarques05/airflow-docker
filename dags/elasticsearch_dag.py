from airflow import DAG
from elasticsearch_plugin.hooks.elastic_hook import ElasticHook
from elasticsearch_plugin.operators.postgres_to_elastic import PostgresToElasticOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2022, 5, 1),
}

def _print_es_info():
    hook = ElasticHook()
    print(hook.info())

with DAG('elasticsearch_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    print_es_info = PythonOperator(task_id='print_es_info', python_callable=_print_es_info)
    connections_to_es = PostgresToElasticOperator(
        task_id='connections_to_es',
        postgres_conn_id='postgres',
        elastic_conn_id='elasticsearch_default',
        sql = 'SELECT * FROM connection',
        index='connections'
    )

    print_es_info >> connections_to_es