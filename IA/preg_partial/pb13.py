from math import sqrt

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
    def get_position(self):
        return (self.x, self.y)
    
    def move(self,action):
        direction = action[0]
        step = action[1]

        match direction:
            case "up" :
                self.y += step
            case "down":
                self.y -= step
            case "right":
                self.x += step
            case "left":
                self.x -= step
            case _:
                print("Invalid direction")
    def distance(self):
        return round(sqrt(self.x * self.x + self.y * self.y))



moves = [
    ("up",5),
    ("down",3),
    ("left",3),
    ("right",2)
]

robot = Robot() 

print(robot.x)
print(robot.get_position())
for item in moves:
    robot.move(item)
print(robot.get_position())
print(robot.distance())