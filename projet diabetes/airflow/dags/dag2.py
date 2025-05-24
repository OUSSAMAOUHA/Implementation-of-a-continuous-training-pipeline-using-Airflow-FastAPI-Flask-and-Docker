from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
import requests
from pytz import timezone
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
import os 
from datetime import datetime
from subprocess import run

# Set the timezone to Casablanca
casablanca_tz = timezone('Africa/Casablanca')

default_args = {
    'owner': 'ghm_group',
    'depends_on_past': False,
    'start_date': datetime.now(casablanca_tz),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Diabetes_App3',
    default_args=default_args,
    description='An Airflow DAG to automize the pipeline',
    schedule_interval='0 */1 * * *',  # Run every 5 minutes
    max_active_runs=1,  # Ensure only one run at a time
    catchup=False,  # Do not run backfill for the intervals between start_date and the current date
)


def check_file_modification(**kwargs):
    file_path = '/opt/airflow/dags/scripts/diabetes.csv'
    modified_time = os.path.getmtime(file_path)
    last_modified = datetime.utcfromtimestamp(modified_time)
    five_minutes_ago = datetime.now() - timedelta(minutes=5)
    return 'execute_python_script' if last_modified >= five_minutes_ago else 'skip_python_script'

def execute_api_task(**kwargs):
    # Assuming your FastAPI application script is named api_script.py
    api_script_path = 'opt.airflow.dags.scripts.APITask'
    uvicorn_command = f"uvicorn {api_script_path}:app --host 0.0.0.0 --port 8000 --reload > /opt/airflow/dags/uvicorn.log 2>&1"
    # Run the uvicorn command
    run(uvicorn_command, shell=True)

# Define the path to the file to be monitored
file_path = '/opt/airflow/dags/scripts/diabetes.csv'  # Replace with the actual path

# Create a FileSensor task to check for changes
file_sensor_task = FileSensor(
    task_id='file_sensor',
    filepath=file_path,
    poke_interval=60,  # Check every 60 seconds
    timeout=600,  # Timeout after 600 seconds (10 minutes)
    mode='poke',
    soft_fail=True,
    dag=dag,
)


check_file_task = BranchPythonOperator(
    task_id='check_file_modification',
    python_callable=check_file_modification,
    provide_context=True,
    dag=dag,
)

python_script_path = '/opt/airflow/dags/scripts/Final_diabetes.py'
python_task = BashOperator(
    task_id='execute_python_script',
    bash_command=f'python {python_script_path}',
    dag=dag,
)

skip_python_task = BashOperator(
    task_id='skip_python_script',
    bash_command='echo "No modification in the last 5 minutes. Skipping script execution"',
    dag=dag,
)

api_task = PythonOperator(
    task_id='execute_api_task',
    python_callable=execute_api_task,
    provide_context=True,
    dag=dag,
)


file_sensor_task >> check_file_task >> api_task
check_file_task >> [python_task , skip_python_task] 