# Online Judge Platform

[![MIT License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

A full-stack Django-based Online Judge platform for coding practice, problem-solving, and automated code evaluation.

## 🚀 Live Demo

Access the deployed platform here: [http://13.127.217.250:8000/auth/login/](http://13.127.217.250:8000/auth/login/)
> ⚠️ Note: The demo may be offline if the EC2 instance is stopped.

---

### 📺 Demo Video

Watch the full walkthrough of the platform here:  
[![Watch the demo](https://img.youtube.com/vi/yG72KlYpnA4/0.jpg)](https://www.youtube.com/watch?v=yG72KlYpnA4)
> 📝 Covers login, problem solving, code evaluation, UI themes, and admin access.<br>
> 💡 Tip: Watch at 1.25x or 1.5x speed for a faster overview!

---

## 📝 Features

- **User Authentication:**
  Secure registration and login with CSRF protection and hashed passwords.
- **Code Submission Engine:** 
  - Supports multiple programming languages (C++, Python)
  - Secure sandboxed execution with timeouts and resource limits
  - Automated evaluation and real-time verdicts (Accepted, Wrong Answer, Time Limit Exceeded, etc.)
- **Submission Tracking:**
  View past submissions, verdicts, and test case results.
- **Admin Interface:**
  Manage coding problems, users, and system settings via the Django admin panel.
- **Responsive UI:**
   Modern interface with dark/light themes and a mobile friendly design.
- **Scalable Deployment:**
  Dockerized for easy setup; deployed on AWS EC2 for reliability and horizontal scaling.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django ORM
- **Frontend:** Django Templates, HTML/CSS (with dark/light themes)
- **Code Execution:** Secure sandboxed engine (multi-language support)
- **Database:** SQLite (for development)
- **Deployment:** Docker, AWS EC2

---

## ⚡ Quick Start

### Prerequisites

- Git (required to clone the repository)
- Python 3.8+
- pip
- Docker (optional, for containerized deployment)
- **Recommended:** Create and activate a virtual environment before installing dependencies
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  ```

### Clone the repository

```bash
git clone https://github.com/rmmukhesh/OnlineJudge.git
cd OnlineJudge/my_project
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables (Local Development Only) 

Create a `.env` file in the project root with the following contents:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Run migrations

```bash
python manage.py migrate

# To create superuser (for admin access)
python manage.py createsuperuser
```

### Start the development server

```bash
python manage.py runserver
```

### Access the app

After starting the development server, you can access:

- **User Login Page:** [http://localhost:8000/auth/login/](http://localhost:8000/auth/login/)
- **Admin Dashboard:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

> ⚠️ Make sure you’ve created a superuser using `python manage.py createsuperuser` to access the admin panel.

---

## 🐳 Docker Deployment

```bash
# Build and run with Docker
docker build -t online-judge .
docker run --env-file .env -d -p 8000:8000 --name con1 online-judge

# To create superuser (for admin access)
# Access the container shell
docker exec -it con1 sh

# Inside container
python manage.py createsuperuser
```

---

## 🌐 AWS Deployment

The platform is deployed on AWS EC2 for scalability and reliability.

### Deployment Summary:
- Launch an EC2 instance (Ubuntu)
- Install Docker
- Clone the repository
- Set up `.env` file
- Run Docker build and start the container

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your forked repo.
5. Open a pull request describing your changes.

Please ensure your code follows best practices and includes relevant tests where possible.

If you have suggestions for features or find any bugs, feel free to open an issue.

Thank you for helping make this project better!

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 👤 Author

- **[Mukhesh RM](https://www.linkedin.com/in/rmmukhesh/)**
- [rmmukhesh@gmail.com](mailto:rmmukhesh@gmail.com)