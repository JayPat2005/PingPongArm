# Tennis Ball Tracker

This Python script utilizes OpenCV to track a tennis ball in real-time using a webcam. It detects the tennis ball based on its color and calculates its position and velocity. The script contains two functions:

1. `track_tennis_ball()`: Tracks the tennis ball using the primary webcam (index 0).
2. `track_tennis_ball_top()`: Tracks the tennis ball using a secondary webcam (index 1), positioned above the playing area.

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- NumPy

Install OpenCV and NumPy using pip:

pip install opencv-python numpy


## Usage

1. Make sure your webcam(s) are connected and functioning properly.
2. Run the script using the following command:

python tennis_ball_tracker.py


3. Press 'q' to quit the program.

## Functionality

- The script detects the tennis ball based on its color (green) using HSV color space.
- It tracks the position of the tennis ball in real-time.
- The position and velocity (in the x and y directions) of the tennis ball are displayed on the video feed.
- The script can handle multiple tennis balls simultaneously.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
