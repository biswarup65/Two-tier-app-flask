# 🐳 Containerized Two-Tier Web Application using Docker & Docker Compose

## 📘 Project Overview
This project demonstrates how to **containerize a two-tier web application** (a frontend web app and a backend database) using **Docker** and **Docker Compose**.  
Additionally, it showcases how to perform **image vulnerability scanning** using **Docker Scout**, helping ensure that the application is both **secure** and **efficient**.

By completing this project, you’ll gain **hands-on experience** with:
- Docker containerization  
- Multi-container orchestration using Docker Compose  
- Networking between containers  
- Image vulnerability scanning and remediation using Docker Scout  

---

## 🧰 Tools & Technologies Required

| Tool | Purpose |
|------|----------|
| **Docker** | For creating and managing containers |
| **Docker Compose** | For defining and running multi-container applications |
| **Docker Scout** | For scanning Docker images for vulnerabilities |
| **Code Editor (VS Code, Atom, etc.)** | For writing and managing source code |
| **Two-Tier Application Source Code** | A simple web app with a database backend (e.g., Flask + MySQL) |

---
## 🎯 Project Objectives

- Containerize both tiers of the application (frontend & database).  
- Use Docker Compose to run both containers together as one stack.  
- Ensure proper network communication between containers.  
- Use Docker Scout to identify and mitigate image vulnerabilities.  

---

## 🚀 Getting Started

## 1️⃣ Clone the Repository
``` bash
git clone https://github.com/<your-username>/two-tier-docker-app.git
cd two-tier-docker-app/

```
## 2️⃣ Build Docker Image
``` bash
docker build -t two-tier-flask-app:latest .
```
## 3️⃣ Run Application with Docker Compose
``` bash
docker-compose up -d
```
## Run Container locally
```bash
docker run -d --name two-tier-flask-app -p 5000:5000 two-tier-flask-app:latest
```
## 4️⃣ Access the Application
Open your browser and visit:
```yml
http://<your-server-ip>:5000
```
## 5️⃣ Verify Running Containers
```bash
docker ps
```
---

## 🧪 Scanning Images with Docker Scout

## 1️⃣ Install Docker Scout (if not already available):
``` bash
docker scout version

```
## 2️⃣ Scan Images for Vulnerabilities:
``` bash
docker scout cves two-tier-flask-app:latest
```
## 3️⃣ View Recommendations and Fixes:
``` bash
Docker Scout provides detailed vulnerability reports and patch recommendations.
```

---

## Common Docker Commands :

## Build and start containers
``` bash
docker-compose up --build -d
```
## Stop and remove containers
``` bash
docker-compose down
```
## View logs
``` bash
docker-compose logs -f
```
## Scan for vulnerabilities
``` bash
docker scout cves <image-name>
```


