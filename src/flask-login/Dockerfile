# pull official base image
FROM python:3.9.1-slim-buster
#FROM python:3.9.1
ADD project /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#ENV FLASK_APP=/app/main.py
ENV FLASK_APP=/app
ENV FLASK_ENV=development
EXPOSE 5000
#ENTRYPOINT ["flask run --host=0.0.0.0"]