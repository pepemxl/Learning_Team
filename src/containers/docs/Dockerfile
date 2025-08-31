FROM python:3.13

WORKDIR /app
COPY src/containers/docs/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY mkdocs.yml /app/
COPY docs/ /app/docs/
EXPOSE 8080
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8080"]