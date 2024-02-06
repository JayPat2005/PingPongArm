import cv2
import numpy as np
import time

# Function to track the tennis ball and draw a tail
def track_tennis_ball():
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

    # Initialize variables for tracking the ball's position and tail
    ball_position = None
    tail = []

    # Set up the histogram criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame from webcam")
            break

        # Convert the frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range of color for a tennis ball (fluorescent yellow/green) in HSV
        lower_tennis_ball = np.array([25, 100, 100])
        upper_tennis_ball = np.array([40, 255, 255])

        # Create a mask for the tennis ball color
        mask = cv2.inRange(hsv, lower_tennis_ball, upper_tennis_ball)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contours are found
        if contours:
            # Get the contour with the maximum area (assuming it's the tennis ball)
            max_contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(max_contour)

            # Convert the x and y coordinates to integers
            center = (int(x), int(y))

            # Draw a circle around the tennis ball
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)  # Green color for tennis ball

            # Update the ball position and add it to the tail with timestamp
            ball_position = center
            tail.append((center, time.time()))

            # Draw the solid tail
            for i in range(len(tail) - 1, 0, -1):
                point, timestamp = tail[i]
                cv2.line(frame, tail[i - 1][0], point, (0, 0, 255), 2)  # Red color for the tail

                # Remove points from the tail after 2 seconds
                if time.time() - timestamp > 2:
                    tail.pop(i - 1)

            # Update the histogram for adaptive color range
            roi = hsv[int(y - radius):int(y + radius), int(x - radius):int(x + radius)]
            hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
            cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
            dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)

            # Update the criteria to improve tracking
            track_window = (int(x - radius), int(y - radius), max(1, int(2 * radius)), max(1, int(2 * radius)))
            ret, track_window = cv2.meanShift(dst, track_window, criteria)
            x, y, w, h = track_window
            center = (int(x + w / 2), int(y + h / 2))

            # Calculate velocity
            if len(tail) > 1:
                dt = tail[-1][1] - tail[-2][1]  # Time difference
                dx = tail[-1][0][0] - tail[-2][0][0]  # Change in x
                dy = tail[-1][0][1] - tail[-2][0][1]  # Change in y

                velocity_x = dx / dt
                velocity_y = dy / dt

                # Display information on the webcam frame
                cv2.putText(frame, f"X: {tail[-1][0][0]}, Y: {tail[-1][0][1]}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(frame, f"VX: {velocity_x:.2f}, VY: {velocity_y:.2f}", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Display the frame along with the black and white mask
        combined_display = np.hstack((frame, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)))
        cv2.imshow("Tennis Ball Tracker", combined_display)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run the tracking function for the tennis ball with velocity calculation
track_tennis_ball()
