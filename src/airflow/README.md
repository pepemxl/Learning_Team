# Airflow

Airflow is a platform to program workflows through:
- Creation
- Scheduling
- Monitoring

using the concept of DAGs (Directed Acyclic Graph) and Operators, which are usually sets of task related with/without dependencies between them to schedule jobs.


These workflows can be accessed via:
- code (python)
- command line (airflow-cli)
- web UI interface


Other examples of workflows platforms are:
- Jenkins: Jenkins is a CI open-source continuous integration server.
- Pachyderm: It is an open source MapReduce engine.
- Argo: It is an open source container-native workflow engine for getting work done.
- Apache NiFi: A powerful and reliable system to process and distribute data.
- Kubeflow: The Kubeflow project is dedicated to making Machine Learning on Kubernetes.
- Kafka: Kafka is a distributed, partitioned, replicated commit log service. It provides
- Datafabric: workflow for cloud doing good use of technologies in cloud.
- Dagster: Similar to Kubeflow oriented to testing microservice development.
- Luigi: It is a Python module that helps you build complex pipelines of batch jobs.
- SSIS: SQL Server Integration Services
- Bash scripting: Always part of whatever RPC system.

## Local Installation on Windows

[install_windows_wsl](./install_windows_wsl.md)

## Docker version

[install_windows_wsl](./install_windows_wsl.md)

## What is a worflow?

A workflow is a set of steps to accomplish a given data engineering task.
- downloading files
- copying data
- filtering data
- writing to database
- etc.


### Example of a workflow
- Sales data workflow
    - Download Sales Data
    - Clean Sales Data
    - Run ML pipeline
    - Upload results
    - Generate Report
    - Email to Chief


These worflows are implemented with DAGs (Directed Acyclic Graph)

## DAGs

DAGs are created with varios details about the DAG:
- name
- start date
- owner
- etc

### Example DAG

```python
etl_dag = DAG(
    dag_id = "etl_pipeline",
    dafault_args={"start_date": "2021-12-05"}
)
```

## Runnning a worflow in Airflow

### Running a task
```bash
airflow run <dag_id> <task_id> <start_date>
```
### Running a full dag
```bash
airflow trigger_dag -e <start_date> <dag_id> 
```

## Basic Commands

- `airflow -h`
- `airflow list_dags`

## Airflow Operators

Operators represent a single task in a workflow. Typically Airflow operator run independently, they do not share information between operators.

- SSHOperator helps, connect to a server over SSH, and executes specified commands
- DockerOperator for executing a command inside the docker container
- HiveOperator for executing HQL code or hive script in a specific Hive DB

### DummyOperator
`DummyOperator(task_id='example', dag=dag)` is used for troubleshooting or for a task that has not been implemented.


### BashOperator
```python
from airflow.operators.bash_operator import BashOperator


example_task_01 = BashOperator(
    task_id='bash_example',
    bash_command='echo "Example"',
    dag=ml_dag
)
```

```python
from airflow.operators.bash_operator import BashOperator


example_task_02 = BashOperator(
    task_id='bash_script_example',
    bash_command='run_some_scripts.sh',
    dag=ml_dag
)
```

## Task Dependencies

Task dependencies are referred as `upstream`(before) or `dowstream`(after) tasks.

- `>>` upstream operator
- `<<` downstream operator

```python
task1 = BashOperator(task_id='first_task',
                    bash_command='echo 1',
                    dag= example_dag
                    )
task2 = BashOperator(task_id='second_task',
                    bash_command='echo 2',
                    dag= example_dag
                    )
task1 >> task2
```

### Multiple Dependencies

`task1 >> task2 >> task3 >> task4`

###  Mixed Dependencies

`task1 >> task2 << task3`

or

```python
task1 >> task2
task3 >> task2
```

## Adiotional Operators

### PyhonOperator

- Executes a Python function / callable
- Operates similarly to the BashOPerator
- Can pass in arguments to the Python code


```python
from airflow.operators.python_operator import PythonOperator

def printme():
    print("Logging something")

python_task = PythonOperator(
    task_id='simple_print',
    python_callable=printme,
    dag=example_dag
)

```

### Arguments

- Positional
- Keyword

`op_kwargs`


```python
from airflow.operators.python_operator import PythonOperator

def sleep(lenght_of_time):
    time.sleep(lenght_of_time)

sleep_task = PythonOperator(
    task_id='sleep',
    python_callable=printme,
    op_kwargs={'lenght_of_time': 5}
    dag=example_dag
)

```

### EmailOperator

- `airflow.operator`

```python
from airflow.operators.email_operator import EmailOperator


email_task = EmailOperator(
    task_id='email_sales_report',
    to='pepemxl@gmail.com',
    subject='this is an automatic report',
    html_content='<h1>This is an automatic Report</h1>',
    files='lastes_report.xlsx',
    dag=example_dag
)

```

some options

```python
default_args={
    'email': ['pepemxl@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'email_on_success': True,  
}
```

## DAG Runs
- A specific instance of a worflow a a point in times is created
- Can be run manually or via `schedule_interval`
- Maintain state for each workflow and the tasjs within
    - running
    - failes
    - success

### Schedule details

- `start_date` The date / time to initially schedule the DAG run
- `end_date` Optional attribute for when to stop running new DAG instances
- `max_tries` Optional attribute for how many attempts to make
- `schedule_interval` How often to run

cron syntax

`* * * * *` 5 fields separated by space

- minute 0 - 59
- hour   0 - 23
- day of the month 1 - 31
- month 1 - 12
- day of the week 0-6(Sunday to Saturday)

@hourly = 0 * * * * 
@daily = 0 0 * * * 
@weekly = 0 0 * * 0

- None - only manual triggered
- @once


`start_date`: datetime(2021,12, 5)
`schedule_interval`: @daily

means that the earliest starting time to tun the DAG would be December 6th, 2021.

## Sensors

- An operator that waits for a certain condition to be true
    - Creation of a file
    - Upload of a database record
    - Certain response from a web request

`airflow.sensors.base_sensor_operator`
- mode - how check for the condition
    - mode = 'poke' - run repeatedly
    - mode = 'reschedule' - give up task slot and retry again later
- poke_interval - how often to wait between checks
- timeout - how long to wait before failing task


### File Sensor

```python
from airflow.contrib.sensors.file_sensor import FileSensor

file_sensor_task = FileSensor(
            task_id = 'file_sense',
            filepath = 'file_input.csv',
            poke_interval = =300,
            dag = report_dag)
init_process >> file_sensor_task >> generate_report
```

### ExternalTaskSensor

Waits for a tasj in another DAG

### HttpSensor

Request a web URL and check for content

### SqlSensor

Runs a SQL query to check for content


## Executor
- Executors run tasks
- Differente executor handle runnning the same task in different ways
    - SequentialExecutor
    - LocalExecutor
    - CeleryExecutor

### Sequential Executor

This is the default Airflow executor, it runs one task at a time, useful for debugging NOT fort production.

### Local Executor

Runs on a sinfle system, treats task as processes. The user setup the limit of simultaneous tasks.

### Celery Executor

Uses a Celery backend as task manager. This permit define use multiple worker systemsfor a given set of workflows or tasks. The only issue with this executor is that needs severals configurations.

To know which one is being used:

```bash
cat ariflow/ariflow.cfq | grep "executor = "
```

## Templates

Templates in airflow works as templates in Flask, they permit us to change/substitute information at moment to render/running a DAG(airflow use Jinja templating language!!!). Mant workflows/task are very similar then these templates permit us to have a DRY code.

Example:
```python
task1 = BashOperator(
    task_id =  'task_01',
    bash_command = 'upload_file_01.sh',
    dag = dag
)
task2 = BashOperator(
    task_id =  'task_02',
    bash_command = 'upload_file_02.sh',
    dag = dag
)
task3 = BashOperator(
    task_id =  'task_03',
    bash_command = 'upload_file_03.sh',
    dag = dag
)
```

Using templates become and asuming a new upload_file.sh who reactives parameters was created:

```python
template_command = """
    upload_file.sh {{params.filename}}
"""
```
```python
task1 = BashOperator(
    task_id =  'template_task',
    bash_command = template_command,
    params={'filename': 'file_01.csv'}
    dag = dag
)
```

a better use of templates using jinja sintax could be 

```python
template_command = """
{% for filename in params.filenames %}
    upload_file.sh {{ filename }}
{% endfor %}
"""

task1 = BashOperator(
    task_id =  'template_task',
    bash_command = template_command,
    params={'filenames': ['file_01.csv', 'file_02.csv']}
    dag = dag
)
```

# Variables

- Runtime variables
- Execution Date: `{{ ds }}`
- Execution Date, no dashes: `{{ ds_nodash }}`
- Previous Execution Date: `{{ prev_ds }}`
- Previous Execution Date, no dashes: `{{ prev_ds_nodash }}`
- Dag Object: `{{ dag }}`
- Airflow config object: `{{ conf }}`
- ...

# Macros
`{{ macros }}`
- `{{ macros.datetime }}`: `datetime.datetime`
- `{{ macros.timedelta }}`: `timedelta`
- `{{ macros.uuid }}`: `uuid`
- `{{ macros.ds_add('2021-12-05', 6) }}`: Modiify days from a date, in this example correspond to 2021-12-11

# Branching

Branching provides the ability for conditional logic within of Airflow. It means that we can execute or skip a task depending of the result of a previous operator.

`from airflow.operators.python_opertor import BranchPythonOperator`

## Example

```python
from airflow.operators.python_opertor import BranchPythonOperator

def condition(**kwargs):
    if int(kwargs['parameter_value']) > 5:
        return 'task_condition_true'
    else:
        return 'task_condition_false'

branch_task = BranchPythonOperator(
    task_id='branch_task',
    dag=dag,
    provide_context=True,
    python_callable=condition
)

start_task >> branch_task
branch_task >> task_condition_true
branch_task >> task_condition_false
```


# Typical problems and solutions


- DAG didn't load
    - Naming problem
    - Incorrect folder, check configuration
- DAG didn't run on schedule
    - Sometimes scheduler is tuned off at this moment something schedule could be skipped
    - Bad Configuration
    - Not enough resources allocated to run task, dependes on configuration of executor
- Sintax
    - run `python3 <id_dag>`


# SLAs

Service Level Agreement, an SLA mmiss is any time the DAG/task/subtask does not meet the experted timing.
```
Browse->Sla Misses
```

To define SLA we can do the next:

```python
task1 = BashOperator(task_id='task_sla',
                    bash_command='upload_file.sh',
                    sla=timedelta(minutes=10),
                    dag = dag)
```
or use defaults
```python
default_arguments={
    'sla': timedelta(minutes=20)
    'start_date':datetime(2021,12,5)
}
dag = DAG('dag_sla', default_args=default_arguments)
```

There a few more special features:

## XCom 

Cross-communication mechanism between tasks, for scenarios where the output of an ETL process serves as an input for another. 

## Backfilling

Running tasks with a custom time frame specified by users. We have the freedom to either backfill the entire DAG or just a particular task in the DAG. We use this property to reprocess historical data after adding a new feature or for coping up with data loss. 

## Concurrency 

Airflow also provides the comfort of managing concurrent parallel tasks as part of the DAG definition. Unlike Jenkins, we didn’t need to click n pages to finally reach the output page in Airflow, since all the scheduled runs associated with the DAGs are available inside the tree view which makes it very easy to navigate and access all the logs.