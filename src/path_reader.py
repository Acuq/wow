import os

class PathReader:
    def read(self, filename):
        script_dir = os.path.dirname(__file__)
        routes_dir = os.path.join(script_dir, "..", 'routes')
        file_path = os.path.join(routes_dir, filename + '.txt')
        x_coordinates = []
        y_coordinates = []
        with open(file_path, 'r') as f:
            for line in f:
                x, y = line.strip().split(', ')
                x_coordinates.append(float(x))
                y_coordinates.append(float(y))
        return x_coordinates, y_coordinates