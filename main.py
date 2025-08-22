class Robot:
    def __init__(self, name, wheel_diameter):
        self.name = name
        self.wheel_diameter = wheel_diameter
        self.is_on = False

    def print_specs(self):
        print(f"Robot Name: {self.name}")
        print(f"Wheel Diameter: {self.wheel_diameter} meters")
        print(f"Status: {'Online' if self.is_on else 'Offline'}")

# Create an object from the Robot class
my_first_robot = Robot(name="MVP-01", wheel_diameter=0.07)

# Use a method from the object
my_first_robot.print_specs()