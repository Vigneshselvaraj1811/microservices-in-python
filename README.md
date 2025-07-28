```markdown
# 🧱 Microservices Project with FastAPI + Docker

This project demonstrates a microservices architecture using **FastAPI**, **Docker**, and **Nginx**. It includes two independent services:

- 📮 `posts_service`: Manages blog posts
- 💬 `comments_service`: Handles comments on posts

Each service is containerized and runs independently, communicating via REST APIs. The services are orchestrated using **Docker Compose** with **Nginx** as the reverse proxy.

---

## 📁 Project Structure


microservices/
├── comments\_service/
│   ├── app/
│   │   ├── **init**.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── database.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── posts\_service/
│   ├── app/
│   │   ├── **init**.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── database.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
└── nginx.conf


---

## 🚀 How to Run

Make sure you have **Docker** and **Docker Compose** installed.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/microservices.git
cd microservices
````

### Step 2: Run All Services

```bash
docker-compose up --build
```

This will:

* Build Docker images for `posts_service` and `comments_service`
* Start both services and Nginx as a reverse proxy

### Step 3: Access APIs

* **Posts API**: [http://localhost/posts/](http://localhost/posts/)
* **Comments API**: [http://localhost/comments/](http://localhost/comments/)

---

## ⚙️ Tech Stack

| Layer      | Technology                |
| ---------- | ------------------------- |
| Language   | Python 3.10+              |
| Framework  | FastAPI                   |
| Web Server | Nginx                     |
| Container  | Docker, Docker Compose    |
| API Docs   | Swagger (auto by FastAPI) |

---

## 📦 API Overview

### Posts Service

| Method | Endpoint  | Description       |
| ------ | --------- | ----------------- |
| GET    | `/posts/` | List all posts    |
| POST   | `/posts/` | Create a new post |
| ...    |           |                   |

### Comments Service

| Method | Endpoint     | Description           |
| ------ | ------------ | --------------------- |
| GET    | `/comments/` | List all comments     |
| POST   | `/comments/` | Add a comment to post |
| ...    |              |                       |

---

## 🧪 Testing

You can test the endpoints using:

* Swagger UI: `http://localhost/docs`
* Postman
* curl

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Future Improvements

* Add authentication with JWT
* Integrate MongoDB or PostgreSQL
* Add a frontend using React or Flutter
* Service-to-service secure communication

---

## 🧑‍💻 Author

Developed by [Vignesh Selvaraj](https://github.com/Vigneshselvaraj1811)

