import os
import sys
import keyboard
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import CoordinateReader, PathRecorder, PathReader, AzimuthCalculator, MouseMover

def main():
    coordinate_reader = CoordinateReader()
    path_recorder = PathRecorder()
    path_reader = PathReader()
    azimuth_calculator = AzimuthCalculator()
    mouse_mover = MouseMover()

    x_p, y_p = path_reader.read("route")
    dir = azimuth_calculator.calculate_azimuth(0,x_p,y_p)

    while True:
        mouse_mover.mouse_move_culc(dir,azimuth_calculator.calculate_azimuth(0,x_p,y_p))
        if keyboard.is_pressed('esc'):
            print("Script stopped.")
            break

if __name__ == "__main__":
    main()