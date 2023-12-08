# main.py
from face_detection import detect_face
from eye_detection import detect_eyes
from eye_detection_function import detect_baby_eyes
from line_notifier import send_line_notification
from camera import start_camera
from utils import *
import time
from camera import *

# Set your LINE Notify access token
token = "GPHKyqGFnz5cF00jwqn2U6sF1kiqXG0Yg2HjGWeTEGI"

# Cooldown duration for face detection (in seconds)
cooldown_duration = 60

# Cooldown duration for eye closed notification (in seconds)
eye_closed_notification_duration = 30


def main():
    cap = start_camera()

    last_face_detection_time = 0
    no_face_detected_time = None
    last_eye_closed_time = None

    while True:
        ret, frame = cap.read()

        # Call function to detect face
        keypoints, confidence_score = detect_face(frame)

        face_detected = False

        if keypoints is not None:
            # Draw bounding box and landmarks
            draw_bounding_box(frame, keypoints['box'])
            draw_landmarks(frame, keypoints['keypoints'])

            # Face is detected
            face_detected = True

            # Check if the baby's eyes are closed
            if detect_baby_eyes(frame, keypoints):
                if last_eye_closed_time is None:
                    # Eyes are closed, start the timer
                    last_eye_closed_time = time.time()
                elif time.time() - last_eye_closed_time >= eye_closed_notification_duration:
                    # Eyes have been closed for more than 30 seconds, send a notification
                    send_line_notification(
                        "Baby's eyes are closed for more than 30 seconds")
                    last_eye_closed_time = None  # Reset the timer
            else:
                # Eyes are open, reset the timer
                last_eye_closed_time = None

        current_time = time.time()

        # Check if a face was detected
        if face_detected:
            if no_face_detected_time is not None:
                # Face was detected after a period of no detection, reset the timer
                no_face_detected_time = None
            if current_time - last_face_detection_time >= cooldown_duration:
                save_frame(frame, "./image_path/frame.jpg")
                send_line_notification(
                    "Face detected", image_path="./image_path/frame.jpg")
                last_face_detection_time = current_time
        else:
            if no_face_detected_time is None:
                # Face not detected, start the timer
                no_face_detected_time = current_time
            elif current_time - no_face_detected_time >= 5:
                # Wait for 5 seconds before sending the notification
                save_frame(frame, "./image_path/frame.jpg")
                send_line_notification(
                    "Can't detect face", image_path="./image_path/frame.jpg")
                no_face_detected_time = None  # Reset the timer

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
