@ECHO OFF
docker-compose up airflow-init
REM The account created has the login airflow and the password airflow.
docker-compose up

