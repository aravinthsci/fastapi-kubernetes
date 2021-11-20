# fastapi-kubernetes

Python FastAPI real time Example with Dockerfile and configuration for Kubernetes


## Development setup
To run:

Run from active Python environment using `uvicorn`:

``python app.py``

Navigate to http://localhost:8080/fastapi to test the API.


![Test drive the API](./resources/fastapi.PNG)

## HowTo dockerize it

1. [Install](https://www.docker.com/get-started) docker.
2. Go to the directory where Dockerfile is
3. `docker build -t fastapi_kubernetes:1.0 .` (don't forget the dot)
4. docker run --name fastapi_kubernetes -d -p 8001:8001 fastapi_kubernetes:1.0

Done! Go to *localhost:8001* to see the app

