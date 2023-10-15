FROM python:3
# set a directory for the app insice of docker image
WORKDIR /usr/src/app
# copy all the files to the container
COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]