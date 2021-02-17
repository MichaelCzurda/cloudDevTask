# cloudDevTask

## Description

This Repository is multi-container Docker applications managed by Docker Compose

## Applications

### Precondition
- installed Docker
- installed Docker Compose

### Getting Strated

1. Load the FastAPI Image from DockerHub
    docker pull 108478/fastapi
2. Load the Python Client Image from DockerHub
    docker pull 108478/client
3. Starting both COntainers as Services
    docker-compose up


### FastAPI 
Web Framework providing one endpoint

#### 

### Client Python
Python Client which calls the endpoint