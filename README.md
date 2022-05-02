# Airflow with Docker

## Purpose

Easy way to run Airflow with Docker (Test purposes). Also, will create an Elasticsearch instance.

The Docker Compose file it's based on this tutorial: [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html).

## Prerequisites

Docker should have at least 6GB of RAM to up the environment.

## Usage

Just run the composer up:

```bash
docker compose -f docker-compose.yaml up -d
```

You will be able to access the Airflow with `http://localhost:8080`. The user and password is `airflow`.

## Airflow Connections

In order to use the DAGs, you need to create some connections. You can create under the WebUI (Admin --> Connections) or using the bash inside the webserver host.

### User Api

| Connection ID | Connection Type | Host |
| ------------- | --------------- | ---- |
| user_api | HTTP | https://randomuser.me/ |

### Postgres

| Connection ID | Connection Type | Host | Schema | Login | Password | Port | Extras |
| ------------- | --------------- | ---- | ------ | ----- | -------- | ---- | ------ |
| postgres | Postgres | postgres | airflow | airflow | airflow | 5432 | `{"cursor":"realdictcursor"}`

### Elasticsearch

| Connection ID | Connection Type | Host | Port |
| ------------- | --------------- | ---- | ---- |
| elasticsearch_default | Elasticsearch | elasticsearch | 9200 |

## Cleanup

To remove the resources, you can run:

```bash
docker compose -f docker-compose.yaml down --volumes
```
