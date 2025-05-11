# Backend Microservice for Review Analysis

This is a backend microservice designed to accept user-submitted product reviews and return AI-generated feedback (simulated for this challenge).

## Technologies Used

* Python
* FastAPI
* Pydantic
* Docker
* Docker Compose
* Pytest

## Local Setup

1.  **Clone this repository:**
    ```bash
    git clone <your_repository_url>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    .\venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application (Without Docker)

1.  Execute the application using Uvicorn:
    ```bash
    uvicorn app.main:app --reload
    ```
2.  The API will be available at `http://localhost:8000`.
3.  You can access the automatic API documentation (Swagger UI) at `http://localhost:8000/docs`.

## Testing

### Unit Tests

1.  Ensure dependencies are installed (especially `pytest`).
2.  Run unit tests from the project root:
    ```bash
    python -m unittest app/tests/test_review_service.py
    ```

### Integration Tests

1.  Ensure dependencies are installed (especially `pytest` and `requests`).
2.  Run integration tests from the project root (ensure the application is running locally):
    ```bash
    pytest app/tests/test_reviews_api.py
    ```

## Docker Setup and Usage (Note: Potential Issue Encountered)

The project includes a `Dockerfile` and `docker-compose.yml` for containerization.

### Docker Requirements

* Docker installed on your system.
* Docker Compose installed on your system.

### Building and Running with Docker

1.  Navigate to the project root in your terminal.
2.  Build and run the Docker container:
    ```bash
    docker-compose up --build
    ```
3.  The API should be accessible at `http://localhost:8000`.

### Note on Docker Issue

During the development of this case study, I encountered a persistent `ModuleNotFoundError: No module named 'app'` when attempting to run the application within the Docker container. I have included the `Dockerfile` and `docker-compose.yml` as requested, and they are configured to copy the application code into the container and run the Uvicorn server. Despite trying various configurations for `WORKDIR`, `COPY`, and `PYTHONPATH` in the `Dockerfile`, the import error persisted within the Docker environment. The application runs successfully outside of Docker in the local development environment. Further investigation into the specific Docker setup or environment might be needed to resolve this issue.

## AI-Assisted Development Tools

During the development of this project, I utilized [**Specify the AI-assisted development tool(s) you used, e.g., GitHub Copilot, Cursor, etc.**].

This tool helped me by:

* [**Example 1: Describe a specific way the AI tool helped, e.g., Suggesting code completions for repetitive tasks.**]
* [**Example 2: Describe another way the AI tool helped, e.g., Providing alternative solutions or suggesting improvements to the code.**]
* [**Example 3: Describe another way the AI tool helped, e.g., Speeding up the writing of boilerplate code or unit tests.**]

Overall, the AI-assisted development tool significantly enhanced my productivity by reducing the time spent on writing certain parts of the code and exploring different implementation approaches more quickly.

## Next Steps (Future AI Integration)

The current architecture is designed with modularity in mind to support future integration with real AI models or external services. This could involve:

1.  Creating a new class (or modifying the existing `AIMockAnalyzer`) to interact with an external AI API (e.g., OpenAI, Google Cloud AI, etc.).
2.  Implementing the necessary logic for API authentication and response processing.
3.  Ensuring the interface of the AI analysis component remains consistent to minimize impact on the `ReviewService`.
4.  Utilizing environment variables or configuration files to manage API keys and other service-specific settings.