from face_detection import detect_face
from eye_detection_function import detect_baby_eyes
from line_notifier import send_line_notification
from camera import start_camera
from utils import *
import time
import cv2

# Cooldown duration for face detection (in seconds)
cooldown_duration = 60

no_face_detected_time = None
last_eye_closed_time = None
waiting_for_eyes = False
screenshot_taken = False
first_open_eyes_after_closed = False

vc = start_camera()
token = "GPHKyqGFnz5cF00jwqn2U6sF1kiqXG0Yg2HjGWeTEGI"

if __name__ == "__main__":
    while True:
        # Read the raw frame without processing
        ret, frame = vc.read()
        if not ret:
            break

        # Call function to detect face
        keypoints = detect_face(frame)

        face_detected = keypoints is not None

        current_time = time.time()

        # Check if a face was not detected
        if keypoints is None:
            if no_face_detected_time is None:
                # Face not detected, start the timer
                no_face_detected_time = current_time
            elif current_time - no_face_detected_time >= 5 and not screenshot_taken:
                # Wait for 5 seconds before sending the notification and take a screenshot
                save_frame(frame, "./image_path/frame.jpg")
                send_line_notification(
                    "Can't detect face", image_path="./image_path/frame.jpg")
                no_face_detected_time = None  # Reset the timer
                screenshot_taken = True
        else:
            # Face was detected, reset the timer and screenshot flag
            no_face_detected_time = None
            screenshot_taken = False
            # Your existing logic for when a face is detected
            face_detected = True

        # Check if the baby's eyes are closed
        if not detect_baby_eyes(frame):
            if last_eye_closed_time is None:
                # Eyes just closed, record the time
                last_eye_closed_time = time.time()
            else:
                elapsed_closed_time = time.time() - last_eye_closed_time
                if elapsed_closed_time >= 3:
                    if not waiting_for_eyes:
                        # Eyes closed for 3 seconds, start waiting
                        waiting_for_eyes = True
                        print("Waiting for eyes!")
                else:
                    # Eyes closed, but not for 3 seconds yet
                    waiting_for_eyes = False
        else:
            if waiting_for_eyes:
                save_frame(frame, "./image_path/frame.jpg")
                send_line_notification(
                    "Eyes open", image_path="./image_path/frame.jpg")
                waiting_for_eyes = False
            # Eyes are open, reset the timers
            last_eye_closed_time = None
            waiting_start_time = None


# Additional logic here (display, etc.)

        cv2.imshow("Output", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

vc.release()
cv2.destroyAllWindows()
