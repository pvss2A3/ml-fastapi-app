# ml-fastapi-app

A FastAPI-based machine learning prediction API with Docker and CI/CD pipeline.

## Features

- Predicts diabetes progression based on patient data
- Built with FastAPI and Pydantic for validation
- Dockerized for easy deployment
- Automated testing with Pytest
- CI/CD with GitHub Actions
- DockerHub integration for image distribution
- Local deployment with Docker Compose

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Git
- (Optional) GitHub account for CI/CD

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/ml-fastapi-app.git
   cd ml-fastapi-app

2. Create and activate a Python virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # macOS/Linux
    .\venv\Scripts\activate    # Windows

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Run the app locally:

    ```bash
    uvicorn api.app:app --reload

Open http://localhost:8000/docs to access API docs.

### Using Docker

1. Build Docker image:
   ```bash
   docker build -t your-dockerhub-username/ml-fastapi-app .

2. Run container:
    ```bash
    docker run -p 8000:8000 your-dockerhub-username/ml-fastapi-app

3. Or use Docker Compose:
    ```bash
    docker compose up --build

### Running Tests
Run Pytest:
   ```bash
   pytest
   ```

### API Usage Example

   ```bash
   curl -X POST http://localhost:8000/predict \
   -H "Content-Type: application/json" \
   -d'{"age":0.038,"sex":0.050,"bmi":0.062,"bp":0.022,"s1":-0.044,"s2":-0.035,"s3":-0.043,"s4":-0.002,"s5":0.020,"s6":-0.018}'



