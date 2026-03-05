from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys
from pathlib import Path

root_path = Path(__file__).parents[1] 
sys.path.append(str(root_path))

from src.utils.reader import read_json
from src.transformers.address_transformer import transform
from src.utils.writer import write_json



def run_etl():
    base_path = os.getenv('AIRFLOW_HOME', '/opt/airflow')
    input_dir = os.path.join(base_path, 'data/int_test_input')
    output_file = os.path.join(base_path, 'data/int_test_output/enriched_output.json')
    api_key = os.getenv("LOCATIONIQ_API_KEY")

    # Extract
    raw_records = read_json(input_dir)
    print("Extraction complete")

    # Transform
    enriched_iterator = transform(raw_records, api_key)
    print("Transformation complete")

    #Load
    write_json(enriched_iterator, output_file)
    print(f"Enriched data successfully written to {output_file}")


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    'etl_geocode',
    default_args=default_args,
    description='ETL pipeline for address enrichment',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl'],
) as dag:

    etl_task = PythonOperator(
        task_id='geocode_etl_task',
        python_callable=run_etl
    )