# Toy Robot Challenge API

This project is a simple API for simulating a robot's movements on a 5x5 grid. The robot can be placed on the grid, moved, and rotated. The API is built using FastAPI.

## Requirements

- Python 3.7+
- FastAPI 0.95.2
- Uvicorn 0.22.0
- Pydantic 1.10.7
- Requests 2.31.0
- Pytest 7.4.0

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Place the Robot

- **Endpoint:** `/place`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "x": 0,
        "y": 0,
        "f": "NORTH"
    }
    ```
- **Description:** Places the robot on the grid at the specified position and facing the specified direction.

### Move the Robot

- **Endpoint:** `/move`
- **Method:** `POST`
- **Description:** Moves the robot one unit forward in the direction it is currently facing.

### Turn the Robot Left

- **Endpoint:** `/left`
- **Method:** `POST`
- **Description:** Rotates the robot 90 degrees to the left.

### Turn the Robot Right

- **Endpoint:** `/right`
- **Method:** `POST`
- **Description:** Rotates the robot 90 degrees to the right.

### Report the Robot's Position

- **Endpoint:** `/report`
- **Method:** `GET`
- **Description:** Returns the current position and direction of the robot.

## Running Tests

1. Run the tests using Pytest:
    ```bash
    pytest
    ```

