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

### Using the Application

After installation, the API will be available at http://localhost:5000

The frontend interface is automatically served by Flask and can be accessed through your web browser.

#### API Overview

For developers, the application exposes a RESTful API at `/tasks` that supports:

- `GET /tasks` - List all tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/:id` - Update a task
- `DELETE /tasks/:id` - Delete a task
- `GET /health` - Health check endpoint

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

#### Health Check (manually)
To check if the container is running correctly:
```bash
curl -i http://localhost:5000/health
```
A status code 200 means the application is healthy.

#### Docker Hub
The image is automatically pushed to Docker Hub only if all tests pass **and** the CI health check is successful (via GitHub Actions, master branch).

## Tests

### Option 1: Local (without Docker)
To run the tests locally:
```bash
pytest tests/
```

### Option 2: With Docker
To run the tests in a dedicated container (full isolation, same environment as CI/CD):
```bash
docker build -f Dockerfile.test -t todo-app-test .
docker run --rm todo-app-test
```

`Dockerfile.test` is dedicated to the testing phase and automatically runs pytest on the `tests/` folder.

## CI/CD Pipeline

The GitHub Actions pipeline is split into two clearly separated phases:

- **Phase 1: Tests**
    - Build a test image with `Dockerfile.test` (runs pytest)
    - If tests fail, the pipeline stops here
- **Phase 2: Build & Deployment**
    - Build the final image with `Dockerfile`
    - Start a local container for health checking (`/health`)
    - If the health check passes, push to Docker Hub (master branch only)
    - Cleanup the health check container

**CI/CD process summary:**

1. Checkout the code
2. Build and run tests with Dockerfile.test
3. Build the final image with Dockerfile
4. Start a container for health check
5. Automatic health check
6. If OK, push to Docker Hub
7. Cleanup

If any step fails, the image is not pushed.

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
