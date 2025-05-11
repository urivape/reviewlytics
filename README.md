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
    git clone https://github.com/urivape/reviewlytics.git
    cd reviewlytics
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
    *(To stop the application, press `Ctrl+C` in the terminal.)*

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

## Docker Setup and Usage

The project includes a `Dockerfile` and `docker-compose.yml` for containerization, making it easy to run the application in a consistent environment.

### Docker Requirements

* Docker installed on your system.
* Docker Compose installed on your system.

### Building and Running with Docker

1.  Navigate to the project root in your terminal.
2.  Build and run the Docker container:
    ```bash
    docker-compose up --build
    ```
3.  The API will be accessible at `http://localhost:8000`.
4.  You can access the automatic API documentation (Swagger UI) at `http://localhost:8000/docs`.

### Stopping Docker Containers

To stop and remove the Docker containers, you can run the following command in the project root:

```bash
docker-compose down
```

## AI-Assisted Development Tools

During the development of this project, I utilized Google's Gemini to enhance my productivity.

Gemini helped me by:

* **Exploring alternative implementation approaches:** When faced with certain design decisions, I used Gemini to brainstorm different ways to structure the code and evaluate the pros and cons of each approach.
* **Understanding specific Python concepts:** Gemini provided explanations and examples for certain Python features and libraries, which helped me to solidify my understanding and implement the code more effectively.
* **Assisting with debugging:** When encountering errors, I used Gemini to get insights into potential causes and suggest possible solutions, speeding up the debugging process.

Overall, Gemini served as a valuable assistant throughout the development process, helping me to explore ideas, understand technical details, and resolve issues more efficiently.

## Next Steps (Future AI Integration)

The current architecture is designed with modularity in mind to support future integration with real AI models or external services. This could involve:

1.  Creating a new class (or modifying the existing `AIMockAnalyzer`) to interact with an external AI API (e.g., OpenAI, Google Cloud AI, etc.).
2.  Implementing the necessary logic for API authentication and response processing.
3.  Ensuring the interface of the AI analysis component remains consistent to minimize impact on the `ReviewService`.
4.  Utilizing environment variables or configuration files to manage API keys and other service-specific settings.