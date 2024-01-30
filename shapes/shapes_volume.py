class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4 / 3) * 3.14 * self.radius ** 3

class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_volume(self):
        return self.side_length ** 3