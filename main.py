# main.py
from Face_Detection.face_detection import detect_face
from Eye_Detection.eye_detection_function import detect_baby_eyes
from line_notifier import send_line_notification
from camera import start_camera
from utils import *
import time

# Set your LINE Notify access token
token = "GPHKyqGFnz5cF00jwqn2U6sF1kiqXG0Yg2HjGWeTEGI"

# Cooldown duration for face detection (in seconds)
cooldown_duration = 60

# Cooldown duration for eye closed notification (in seconds)
eye_opened_notification_duration = 3


def main():
    cap = start_camera()

    no_face_detected_time = None
    last_eye_closed_time = None
    eyes_closed_duration = 10
    waiting_for_eyes = False
    screenshot_taken = False
    first_open_eyes_after_closed = False

    while True:
        ret, frame = cap.read()

        # Call function to detect face
        keypoints, confidence_score = detect_face(frame)

        face_detected = keypoints is not None

        current_time = time.time()

        # Check if a face was not detected
        if not face_detected:
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

        # Check if the baby's eyes are closed
        if not detect_baby_eyes(frame):
            if last_eye_closed_time is not None:
                # Eyes were closed, and there was a previous open time
                elapsed_time_since_closed = current_time - last_eye_closed_time

                if elapsed_time_since_closed >= eyes_closed_duration:
                    waiting_for_eyes = True
                    screenshot_taken = False
                    first_open_eyes_after_closed = True  #
            else:
                # Eyes are closed, reset the timer
                last_eye_closed_time = current_time
        else:
            # Eyes are closed, reset the timer
            last_eye_closed_time = None
            if waiting_for_eyes:
                if first_open_eyes_after_closed:
                    first_open_eyes_after_closed = False
                else:
                    save_frame(frame, "./image_path/frame.jpg")
                    send_line_notification(
                        "Baby's eyes have opened", image_path="./image_path/frame.jpg")
                    last_eye_closed_time = None  # Reset the timer
                    screenshot_taken = True
                    waiting_for_eyes = False

        # Display confidence score at the top in red font
        cv2.putText(frame, f"Confidence: {confidence_score:.2f}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        display_frame("Camera", frame)

        # Wait for a key event and check if the "Esc" key (ASCII code 27) is pressed
        key = wait_key(1)
        if key == 27:  # 27 is the ASCII code for the "Esc" key
            break

    release_resources(cap)


if __name__ == "__main__":
    main()
