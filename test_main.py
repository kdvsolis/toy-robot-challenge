import pytest
from fastapi.testclient import TestClient
from main import app, Position, Direction, robot

client = TestClient(app)

def test_place_robot():
    response = client.post("/place", json={"x": 0, "y": 0, "f": "NORTH"})
    assert response.status_code == 200
    assert response.json() == {"message": "Robot placed successfully"}
    assert robot.position == Position(x=0, y=0, f=Direction.NORTH)

def test_move_robot():
    client.post("/place", json={"x": 0, "y": 0, "f": "NORTH"})
    response = client.post("/move")
    assert response.status_code == 200
    assert response.json() == {"message": "Robot moved successfully"}
    assert robot.position == Position(x=0, y=1, f=Direction.NORTH)

def test_turn_left():
    client.post("/place", json={"x": 0, "y": 0, "f": "NORTH"})
    response = client.post("/left")
    assert response.status_code == 200
    assert response.json() == {"message": "Robot turned left"}
    assert robot.position.f == Direction.WEST

def test_turn_right():
    client.post("/place", json={"x": 0, "y": 0, "f": "NORTH"})
    response = client.post("/right")
    assert response.status_code == 200
    assert response.json() == {"message": "Robot turned right"}
    assert robot.position.f == Direction.EAST

def test_report_position():
    client.post("/place", json={"x": 1, "y": 2, "f": "EAST"})
    response = client.get("/report")
    assert response.status_code == 200
    assert response.json() == {"x": 1, "y": 2, "f": "EAST"}

def test_move_out_of_bounds():
    client.post("/place", json={"x": 4, "y": 4, "f": "NORTH"})
    response = client.post("/move")
    assert response.status_code == 200
    assert response.json() == {"message": "Robot moved successfully"}
    assert robot.position == Position(x=4, y=4, f=Direction.NORTH)

def test_report_without_placing():
    response = client.get("/report")
    assert response.status_code == 400
    assert response.json() == {"detail": "Robot is not placed on the table"}
