import math

class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("The side 'side_a' must be greater than 0.")
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("The angle 'angle_a' must be between 0 and 180 degrees.")
        elif name == "angle_b":
            raise AttributeError("'angle_b' is calculated automatically and cannot be set directly.")

        super().__setattr__(name, value)

    @property
    def angle_b(self):
        return 180 - self.angle_a

    @property
    def area(self):
        return self.side_a ** 2 * math.sin(math.radians(self.angle_a))

    def __str__(self):
        return (f"Rhombus: side_a = {self.side_a}, angle_a = {self.angle_a}, "
                f"angle_b = {self.angle_b}, area = {self.area:.2f}")

try:
    rhombus = Rhombus(10, 60)
    print(rhombus)

    print(f"Opposite angle (angle_b): {rhombus.angle_b}")
    print(f"Area: {rhombus.area:.2f}")

except Exception as e:
    print(f"Error: {e}")