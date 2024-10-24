import math
from coordinate_reader import CoordinateReader

class AzimuthCalculator:
    def __init__(self):
        self.coordinate_reader = CoordinateReader()

    def calculate_azimuth(self, waypoint, x_point, y_point):
        x_current, y_current = self.coordinate_reader.current_char_position()

        if x_current is None or y_current is None:
            print("Не удалось получить текущие координаты")
            return None

        dx = x_point[waypoint] - x_current
        dy = y_point[waypoint] - y_current
        radians = math.atan2(dy, dx)
        degrees = math.degrees(radians * 2)

        print(degrees)
        return degrees