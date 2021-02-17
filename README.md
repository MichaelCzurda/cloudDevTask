# cloudDevTask

## Description

This Repository is multi-container Docker applications managed by Docker Compose

## Applications

### Precondition
- installed Docker
- installed Docker Compose

### Getting Strated

1. Load the FastAPI Image from DockerHub
```
    docker pull 108478/fastapi
```
2. Load the Python Client Image from DockerHub
```
    docker pull 108478/client
```
3. Starting both COntainers as Services
```
    docker-compose up
```

### FastAPI 
Web Framework providing one endpoint for returning a list of integeres in descending order. <br/>
Secret can be sent as API Key in the Header or Query Parameter. <br/>
Secret Key: **"secret"** <br/>
Secret Value: **"1234567890123456789012345678901234567890"**


### Client Python
Python Client which calls the endpoint. The Client is an CLI Python Application an takes the following Arguments

1. Positional Arguments
```
    values - List of Integer Values
    secret - Provided API Key
```
2. Optional parameters
```
    --endpoint - Specify the endpoint to send the request to
```
#### Example Call
```
    docker exec -it clouddevtask_client_1 python app.py "[4,6,34,56,876,78,54,335]" "1234567890123456789012345678901234567890"

```