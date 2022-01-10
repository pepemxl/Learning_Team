FROM python:3.7-alpine
# The FLASK_APP environment variable is the name of the module to import at flask run
ENV FLASK_APP app.py
# "development" is equal to "debug mode", the server will automatically reload if code changes
ENV FLASK_ENV development
# make the server publicly available simply by adding --host=0.0.0.0 to the command line
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 5000

CMD [ "flask", "run" ]
