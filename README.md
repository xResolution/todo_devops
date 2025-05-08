# Todo List Application with CI/CD Pipeline

A simple web application for task management with a complete CI/CD pipeline.

## Architecture

### Backend
- Python 3.9+ with Flask
- Simple REST API
- In-memory storage

### Frontend
- HTML/CSS/JavaScript (Vanilla JS)
- Simple and responsive user interface

### Infrastructure
- Docker for containerization
- GitHub Actions for CI/CD
- Pytest for testing

## Features

### Backend (REST API)
- POST /tasks : Add a new task
- GET /tasks : List all tasks
- PUT /tasks/<id> : Mark a task as completed
- DELETE /tasks/<id> : Delete a task
- GET /health : Health monitoring endpoint

### Frontend
- Simple user interface
- Add new tasks
- Display task list
- Mark tasks as completed
- Delete tasks

## Installation

### Prerequisites
- Python 3.9+
- Docker
- GitHub account
- UV (Universal Virtualenv)

### Option 1: Local Installation (without Docker)

1. Clone the repository
```bash
git clone [your-url]
cd todo_devops
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app/__init__.py
```

The application will be available at http://localhost:5000

### Option 2: Containerized Installation (with Docker)

1. Build the Docker image
```bash
docker build -t todo-app .
```

2. Run the container
```bash
docker run -p 5000:5000 todo-app
```

The application will be available at http://localhost:5000

## Tests

To run the tests:
```bash
pytest tests/
```

## CI/CD Pipeline

The GitHub Actions pipeline performs the following steps:
1. Build and tests
2. Docker image build
3. Push to registry
4. Simulated deployment
5. Health check

## Project Structure
```
todo_devops/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
├── tests/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```
