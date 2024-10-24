import time
import keyboard
import os
from coordinate_reader import CoordinateReader

class PathRecorder:
    def __init__(self):
        self.coordinate_reader = CoordinateReader()

    def record(self):
        print("Кнопка - n отвечает за сохранение координаты. Кнопка - j отвечает за сохранение маршрута")
        x_coordinates = []
        y_coordinates = []
        while True:
            if keyboard.is_pressed('n'):
                time.sleep(1)
                x_value, y_value = self.coordinate_reader.current_char_position()
                if x_value is not None and y_value is not None:
                    x_coordinates.append(x_value)
                    y_coordinates.append(y_value)
                    print("Координаты сохранены")

            if keyboard.is_pressed('j'):
                time.sleep(1)
                filename = input("Введите название маршрута - ")
                script_dir = os.path.dirname(__file__)
                routes_dir = os.path.join(script_dir, 'routes')
                if not os.path.exists(routes_dir):
                    os.makedirs(routes_dir)
                file_path = os.path.join(routes_dir, filename + '.txt')
                with open(file_path, 'w') as f:
                    for i in range(len(x_coordinates)):
                        f.write(f"{x_coordinates[i]}, {y_coordinates[i]}\n")
                print("Координаты сохранены в папку routes")
                break