## Todo APP API
A simple Todo application built using FastAPI and PostgreSQL, with Alembic for database migrations, Docker for containerization, Poetry for dependency management, and a Makefile for task automation.

### Features
- FastAPI for building fast web APIs.
- PostgreSQL as the database to store Todo items.
- Alembic for handling database migrations.
- Docker for easy containerization and deployment.
- Poetry for managing dependencies and packaging.
- Pre-commit hooks for enforcing code quality and consistency before committing code.

### Prerequisites
Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Poetry ](https://python-poetry.org/)
- [Make](https://makefiletutorial.com/)
- [Pre-commit](https://pre-commit.com/)(for managing hooks) 

### Getting Started
Clone the repository
 ```shell
 git clone https://github.com/Marlinekhavele/TODOAPI.git

 cd TODOAPI
 ```

### Set up dependencies with Poetry
Poetry is used for managing the Python dependencies. You can install them with:
 ```shell
 poetry install
 ```

### Install pre-commit hooks
Pre-commit hooks help enforce code quality before committing changes.
To install and configure pre-commit hooks:
1. Install pre-commit globally:
 ```shell
pip install pre-commit
 ```
2. Install the pre-commit hooks:
 ```shell
 pre-commit install
 ```
3. Run all hooks on all files (initial check):
 ```shell
 pre-commit run --all-files
 ```

### Pre-commit Hooks Overview
The following pre-commit hooks are configured for this project to ensure code quality:
- Code Style: Automatically formats code using black, sorts imports with isort, and checks for PEP 8 compliance with flake8.
- Code Quality: Verifies that docstrings are present, removes trailing whitespace, checks for correct Python syntax, and ensures logging is used correctly.
- Configuration Validation: Checks the correctness of TOML and YAML files, and ensures the Poetry configuration is set up properly.

### Docker Setup
Docker is used to containerize the application and the database. First, ensure Docker is running.
Build and Start All Containers
To build and start both the FastAPI application and the PostgreSQL database in Docker containers, use:
 ```shell
 docker-compose up --build
 ```
Start the Database
To start the PostgreSQL database in a Docker container, use the following command:
 ```shell
 make start
 ```
### Running the Application
Once the Docker containers are up and running, the FastAPI application will be accessible at http://localhost:8050.
To start the FastAPI app in development mode (with auto-reload):
 ```shell
 make serve
 ```
### Running Tests
To run tests, the Makefile provides a few options:
1. Run Tests:
To run all the tests using pytest:
 ```shell
 make test
 ```
This will execute tests on the project after ensuring the database migrations are applied using `alembic`.
2. Run Tests with Coverage:
To run tests with coverage reporting (it will show how much of the code is covered by tests):
 ```shell
make test-with-coverage
 ```
This will execute tests with coverage tracking, outputting the results to the terminal and generating an XML report for further analysis.
3. Run Tests with Coverage and Generate Reports:
This command also generates coverage and test run reports in `.test-reports/coverage.xml` and `.test-reports/test-run.xml`:
 ```shell
make test-with-coverage
 ```
It ensures you have detailed test results and code coverage analysis.
















