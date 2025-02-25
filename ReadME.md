# Dockerized Python Sample Application

This project is a simple **Django application** running inside **Docker containers** with **MySQL** as the database. It also uses **mounted volumes** for persistent storage.

## 🚀 Features

- Django application containerized with Docker.
- MySQL database running in a separate container.
- Volumes mounted for persistent database and application data.
- Easy setup with Docker Compose.

## 🛠 Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🏗 Project Structure

```
/PROJECT
│── /Learing/       # Django application source code
│── docker-compose.yml # Docker Compose configuration
│── Dockerfile        # Dockerfile for Django application
│── .env              # Environment variables
│── requirements.txt  # Python dependencies
│── README.md         # Project documentation
```

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gishwinantony/docker-python-deploy.git
cd docker-python-deploy
```

### 2️⃣ Configure Environment Variables

Configure the `.env` file and set up required variables:

```env
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=mydatabase
MYSQL_USER=myuser
MYSQL_PASSWORD=mypassword
```

### 3️⃣ Build & Start the Containers

```bash
docker-compose up --build -d
```


### 4️⃣ Access the Application

- **Django App**: `http://localhost:8000`
- **MySQL Database**: `localhost:3306`

## 🛑 Stopping the Containers

```bash
docker-compose down
```

## 📌 Notes

- Ensure Docker and Docker Compose are installed before running the project.
- The database volume ensures persistent data even if containers are restarted.
- Modify `.env` variables as needed.

---

🚀 **Happy Coding!** 🎉

