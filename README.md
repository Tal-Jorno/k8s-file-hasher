# K8s File Hasher – Scheduled SHA256 CronJob

## Overview
This project defines a Kubernetes CronJob that runs every 15 minutes to process text files in a specified directory:
- It computes a SHA-256 hash of the file content
- Appends the hash to the file
- Renames the file with a timestamp

The logic is implemented in Python, packaged into a Docker image, and deployed via Kubernetes manifests located in the `k8s/` folder.

---

## Project Structure

```
.
├── Dockerfile
├── Hezi_Exe.py
├── jenkinsfile
└── k8s/
    ├── configMap.yaml
    └── cronjob.yaml
```

---

## Components

### `Hezi_Exe.py`
Python script that:
- Reads all `.txt` files from a folder (`HASH_FOLDER`)
- Appends a SHA-256 hash to the end of each file
- Renames the file to `filename_YYYYMMDD_HHMMSS.txt`
- Skips files that already include a timestamp

### `Dockerfile`
Builds a container image that runs the script.

### `jenkinsfile`
Optional CI/CD pipeline definition for building and deploying the image.

### `k8s/configMap.yaml`
Defines the `HASH_FOLDER` environment variable to point to the input folder inside the container.

### `k8s/cronjob.yaml`
Defines a Kubernetes `CronJob` that:
- Runs every 15 minutes
- Mounts a hostPath volume to access real files on the host
- Runs the containerized script on a schedule

---

## How to Run

### 1. Build the Docker Image
```bash
docker build -t hasher:1.0 .
```

### 2. Load Image into Minikube
```bash
minikube image load hasher:1.0
```

### 3. Apply Kubernetes Configuration
```bash
kubectl apply -f k8s/configMap.yaml
kubectl apply -f k8s/cronjob.yaml
```

### 4. Verify Job Execution
```bash
kubectl get cronjob
kubectl get jobs
kubectl get pods
kubectl logs <pod-name>
```

---

## Example File Output

Original:
```
hello world
```

After processing:
```
hello world
***
787EC76DCAFD20C1908EB0936A12F91EDD105AB5CD
***
```
