# main_image.py
import os

from Face_Detection.face_detection import detect_face
from Eye_Detection.eye_detection_function import detect_baby_eyes
from line_notifier import send_line_notification
from utils import *
import time

# Set your LINE Notify access token
token = "GPHKyqGFnz5cF00jwqn2U6sF1kiqXG0Yg2HjGWeTEGI"

# Cooldown duration for eye closed notification (in seconds)
eye_opened_notification_duration = 3


def process_image(image_path):
    # Read the image
    frame = cv2.imread(image_path)

    # Call function to detect face
    keypoints, confidence_score = detect_face(frame)

    face_detected = keypoints is not None

    # Check if a face was not detected
    if not face_detected:
        send_line_notification("Can't detect face", image_path=image_path)
        return

    # Check if the baby's eyes are closed
    if not detect_baby_eyes(frame):
        elapsed_time_since_closed = 0  # Initialize to 0 for a single image

        # Eyes were closed, send a notification
        send_line_notification("Baby's eyes are closed", image_path=image_path)
    else:
        # Eyes are open
        send_line_notification("Baby's eyes are open", image_path=image_path)

    # Send a notification regardless of the eyes being open or closed
    if face_detected and detect_baby_eyes(frame):
        send_line_notification("Baby is sleeping", image_path=image_path)


def process_images_in_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            process_image(image_path)


if __name__ == "__main__":
    # Example usage with a folder path
    folder_path = "./openeyes"
    process_images_in_folder(folder_path)
