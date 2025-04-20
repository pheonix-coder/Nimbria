# Nimbria - Backend

## Installation

1.  Clone the repository.
2.  Navigate to the `server` directory: `cd server`
3.  Create a virtual environment: `python3 -m venv venv`
4.  Activate the virtual environment: `source venv/bin/activate`
5.  Install the dependencies: `pip install -r requirements.txt`

## Running the application

1.  Activate the virtual environment: `source venv/bin/activate`
2.  Run the application: `uvicorn app.app:app --reload`

## Running tests

1.  Ensure you are in the project root directory (parent directory of `server`).
2.  Activate the virtual environment: `source server/venv/bin/activate`
3.  Run the tests: `PYTHONPATH=server pytest`

## Database

The application uses SQLite for data storage. The database file is `nimbria.db` for production and `test.db` for testing.
