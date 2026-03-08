from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.extract import extract_stock_data
from src.transform import transform_stock_data
from src.load import load_to_postgres

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

dag = DAG(
    "stock_data_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
)

extract_task = PythonOperator(
    task_id="extract_stock_data",
    python_callable=extract_stock_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id="transform_stock_data",
    python_callable=transform_stock_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id="load_stock_data",
    python_callable=load_to_postgres,
    dag=dag,
)

extract_task >> transform_task >> load_task