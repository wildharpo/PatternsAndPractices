from Encapsulation.circle import *

if __name__ == "__main__":
    circle = Circle(10)
    print(f"Initial radius: {circle.radius}")

    circle.radius = 15
    print(f"New radius: {circle.radius}")