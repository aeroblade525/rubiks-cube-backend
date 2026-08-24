# Rubik's Cube Solver — Backend

FastAPI backend for the [Rubik's Cube Solver](https://github.com/aeroblade525/Rubik-s-Cube) project. Implements the Pochmann blindfold method using BFS pathfinding to compute a solution for a given cube state.

## Tech stack
- Python 3.11
- FastAPI + Uvicorn

## Running locally (without Docker)

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## API

**POST `/solve`**

Request body:
```json
{ "cube": [...] }
```

Response:
```json
{ "solution": [...] }
```

## Running with Docker

```bash
docker build -t rubiks-solver:v1 .
docker run -p 8000:8000 rubiks-solver:v1
```

## Running with Kubernetes (local dev via minikube)

This backend is meant to run alongside the [frontend](https://github.com/aeroblade525/Rubik-s-Cube), both as pods in a local minikube cluster. See the [frontend README](https://github.com/aeroblade525/Rubik-s-Cube#running-with-kubernetes-local-dev-via-minikube) for the full setup — the short version:

> **Note:** written for Windows + PowerShell + Docker Desktop's `docker` driver.

```powershell
minikube docker-env | Invoke-Expression
docker build -t rubiks-solver:v1 .
kubectl apply -f k8s/backend-deployment.yaml
```

Expose it locally with its own tunnel (needed on Windows since NodePorts aren't directly reachable from the host):
```powershell
minikube service solver-service --url
```
Keep that terminal open — the printed `http://127.0.0.1:XXXXX` URL is what the frontend needs to build against.

## CORS

CORS is configured to allow any `localhost`/`127.0.0.1` origin on any port, since the exact port varies (Vite dev server, minikube tunnels). See `app/main.py`.

## Project structure
```
app/            FastAPI app and routes
algorithms/     Solver logic (Pochmann method, BFS)
k8s/            Kubernetes deployment and service manifests
Dockerfile
requirements.txt
```
