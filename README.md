# 🧩 Find The Word – Python Word Search Game

A simple and interactive **word search puzzle game** built using **Python (Flask)** with a web interface. The game is containerized using **Docker** and deployed on an **AWS EC2 instance** using a **Jenkins CI/CD pipeline**.

This project is designed as a beginner‑friendly **DevOps + Python web app showcase**, covering end‑to‑end development, containerization, and automated deployment.

---

## 🎮 Game Overview

* Home page with category selection
* Categories available:

  * 🍎 Fruits
  * 🎨 Colors
  * 👩‍💼 Professions
  * 🚗 Vehicles
* Each category contains:

  * A word search puzzle grid
  * Hidden words related to the category
  * Input box to check guessed words
  * Result feedback (Correct / Try again)
  * ⬅ Back to Home button

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Containerization:** Docker
* **CI/CD:** Jenkins (Declarative Pipeline)
* **Cloud:** AWS EC2 (Ubuntu)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
word-search-game/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── fruits.html
│   ├── colors.html
│   ├── professions.html
│   └── vehicles.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🚀 How the Application Works

1. User opens the home page
2. Selects a category
3. A puzzle grid is displayed
4. User enters a word guess
5. Backend validates the word
6. Result is shown on the UI

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t word-game .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 --name word-game word-game
```

Access the app:

```
http://3.128.26.178:5000
```

---

## 🔁 Jenkins CI/CD Pipeline

The Jenkins pipeline performs the following steps:

1. Checkout code from GitHub
2. Build Docker image
3. Stop & remove existing container (if running)
4. Run the latest Docker container
5. Deploy updated application automatically

Pipeline file: `Jenkinsfile`

---

## ☁️ AWS Deployment

* Jenkins installed on EC2
* Docker installed on EC2
* Application exposed on port **5000**
* Security group allows inbound traffic on port **5000**

---

## 🎯 Learning Outcomes

* Flask web application development
* HTML/CSS templating
* Docker containerization
* Jenkins CI/CD pipeline creation
* AWS EC2 deployment
* Real‑world DevOps workflow

---

## 👩‍💻 Author

**Sejal Umredkar**
DevOps & Cloud Enthusiast 🌩️

---

## ⭐ Future Improvements

* Responsive design
* Score tracking
* Highlight found words
* User authentication
* Kubernetes deployment

---

✨ *This project is built for learning, practice, and showcasing DevOps skills.*
