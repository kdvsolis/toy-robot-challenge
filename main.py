from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

class Direction(str, Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

class Position(BaseModel):
    x: int = Field(ge=0, le=4)
    y: int = Field(ge=0, le=4)
    f: Direction

class Robot:
    def __init__(self):
        self.position = None

    def place(self, position: Position):
        self.position = position

    def move(self):
        if self.position:
            if self.position.f == Direction.NORTH and self.position.y < 4:
                self.position.y += 1
            elif self.position.f == Direction.SOUTH and self.position.y > 0:
                self.position.y -= 1
            elif self.position.f == Direction.EAST and self.position.x < 4:
                self.position.x += 1
            elif self.position.f == Direction.WEST and self.position.x > 0:
                self.position.x -= 1

    def left(self):
        if self.position:
            directions = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
            self.position.f = directions[(directions.index(self.position.f) + 1) % 4]

    def right(self):
        if self.position:
            directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
            self.position.f = directions[(directions.index(self.position.f) + 1) % 4]

    def report(self):
        if self.position:
            return self.position
        else:
            raise HTTPException(status_code=400, detail="Robot is not placed on the table")

robot = Robot()

@app.post("/place")
def place_robot(position: Position):
    robot.place(position)
    return {"message": "Robot placed successfully"}

@app.post("/move")
def move_robot():
    robot.move()
    return {"message": "Robot moved successfully"}

@app.post("/left")
def turn_left():
    robot.left()
    return {"message": "Robot turned left"}

@app.post("/right")
def turn_right():
    robot.right()
    return {"message": "Robot turned right"}

@app.get("/report")
def report_position():
    return robot.report()
