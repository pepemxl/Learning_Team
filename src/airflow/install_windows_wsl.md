### Step 1: Installing Linux Subsystem (Ubuntu)
- Enable Developer Mode
- Enable Linux Subsystem
- [Download C++ Build Tools (14.0)](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### Step 2: Installing PIP
```bash
sudo apt-get install software-properties-common 
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-setuptools
sudo apt install python3-pip
sudo -H pip install --upgrade pip
```

### Step 3: Installing Dependencies


```bash
sudo apt-get install libmysqlclient-dev 
sudo apt-get install libssl-dev 
sudo apt-get install libkrb5-dev 
sudo apt-get install libsasl2-dev 
```

### Step 4: Installing PostgreSQL

```bash
sudo apt-get install postgresql postgresql-contrib
```
Start the PostgreSQL service
```bash
sudo service postgresql start
```

Next, check the status of the cluster and make sure that it is running. Use the following command. You should get an output that looks something like the screenshot below.
```bash
pg_lsclusters
```

```bash
pg_lsclusters
Ver Cluster Port Status Owner    Data directory              Log file
12  main    5432 online postgres /var/lib/postgresql/12/main /var/log/postgresql/postgresql-12-main.log
```

We will need to extract a few things from this response for the next piece of code. You want to get the version and the cluster then insert those values in the following piece of code:

```bash
sudo pg_ctlcluster <version> <cluster> start
```

then in my case

```bash
sudo pg_ctlcluster 12 main start
```

Once completed, we can now create a database for Airflow to use. Execute the following command to access psql.
```bash
sudo -u postgres psql
```

Next, we need to create a profile and assign the correct privileges.

```bash
CREATE ROLE ubuntu;
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES on database airflow to ubuntu;
ALTER ROLE ubuntu SUPERUSER;
ALTER ROLE ubuntu CREATEDB; 
ALTER ROLE ubuntu LOGIN;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to ubuntu;
```


Now we need to setup a password for the ubuntu user:

```bash
\password ubuntu
```

Now you can type `\q` to quit.

Next, we can connect to the Airflow database and verify the connection information. After running the following script you should receive a response that says “You are now connected..”
```bash
sudo -u postgres psql
postgres=# \c airflow
```

```bash
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# \c airflow
You are now connected to database "airflow" as user "postgres".
airflow=#
```

```bash
airflow=# \conninfo
You are connected to database "airflow" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```

Stop and go to:
```bash
cd /etc/postgresql/*/main/

ls
```

```bash
/etc/postgresql/12/main$ ls
conf.d  environment  pg_ctl.conf  pg_hba.conf  pg_ident.conf  postgresql.conf  start.conf
```

From here we need to modify some values in this config file to finish setting up Airflow. Use the following command to enter the editor:
```bash
sudo nano pg_hba.conf
```
Modify the line underneath #IPv4 local connections to 0.0.0.0/0


Type Ctrl + S to save and Ctrl + X to exit.

Then, we need to use the same command to open another config file.
```bash
sudo nano postgresql.conf
```
Under the “CONNECTIONS AND AUTHENTICATION” section, modify the following

listen_addresses = ‘*’ 


Type Ctrl + S to save and Ctrl + X to exit.

Finally, restart PostgreSQL to save and load the changes.
```bash
sudo service postgresql restart
```

## Step 5: Installing Apache Airflow

To install Airflow, run the following command in the terminal:
```bash
sudo SLUGIFY_USES_TEXT_UNIDECODE=yes pip install apache-airflow
```

Change the <username> parts to your username and then copy the entire line and paste it on a new line within the variables list. Click OK to save the changes.
```bash
export PATH=$PATH:/home/<username>/.local/bin
sudo SLUGIFY_USES_TEXT_UNIDECODE=yes pip install apache-airflow
```

## Step 6: Apache Airflow Setup

1. The following command will initialize the database.

```bash
airflow db init
```
Once completed, the necessary config files will be created in the airflow directory. 
`cd /home/<username>/airflow`
`sudo nano airflow.cfg`

Make the following changes to the config file:
```
dags_folder = /mnt/c/dags
base_log_folder = /mnt/c/dags/logs
executor = CeleryExecutor
load_examples = False
expose_config = True
sql_alchemy_conn = postgresql+psycopg2://ubuntu:<password>@localhost:5432/airflow
broker_url = amqp://guest:guest@localhost:5672//
result_backend = amqp://guest:guest@localhost:5672//
```
**Insert the password you created in the previous step in the `<password>` section of the sql_alchemy_conn value

Use Ctrl + S to save and Ctrl + X to exit.

in case of error with library `psycopg2`
```
 python3 -m pip install psycopg2-binary
```

after `airflow db init` you shouw see next message:

`Initialization done`


If you receive an error relating to the psycopg2 package, run the following commands to correct this issue:

sudo apt-get update -ysudo apt-get install -y libpq-devpip install psycopg2

#### Install Rabbitmq

sudo apt install rabbitmq-server

We need to update the config file. Navigate to the rabbitmq config file and change the following:

sudo nano /etc/rabbitmq/rabbitmq-env.conf

Change NODE_IP_ADDRESS=0.0.0.0

Now start the RabbitMQ service.

sudo service rabbitmq-server start

#### Install Celery

There are newer versions of Celery that are not compatible with airflow. The following command will install a lower version that ensures compatability.

sudo pip install 'celery>=3.1.17,<4.0'

#### Install Kubernetes dependencies

pip install apache-airflow['cncf.kubernetes']

pip install apache-airflow['cncf.virtualenv']

sudo pip install virtualenv

Run Airflow db init one last time:

airflow db init

:/mnt/c/Users/pepem$ airflow db init
DB: postgresql+psycopg2://ubuntu:***@localhost:5432/airflow
/usr/local/lib/python3.8/dist-packages/sqlalchemy/dialects/postgresql/base.py:3571 SAWarning: Predicate of partial index idx_dag_run_queued_dags ignored during reflection
/usr/local/lib/python3.8/dist-packages/sqlalchemy/dialects/postgresql/base.py:3571 SAWarning: Predicate of partial index idx_dag_run_running_dags ignored during reflection
[2021-12-05 21:56:20,269] {db.py:910} INFO - Creating tables
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
WARNI [airflow.models.crypto] empty cryptography key - values will not be stored encrypted.
Initialization done