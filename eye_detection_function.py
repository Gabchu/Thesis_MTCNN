# eye_detection_function.py
from eye_detection import detect_eyes


def detect_baby_eyes(frame, keypoints):
    landmarks = {'left_eye': keypoints['left_eye'],
                 'right_eye': keypoints['right_eye']}

    eyes_info = detect_eyes(frame, landmarks)

    # Set a threshold for closed eyes
    eye_closed_threshold = 0.25  # Adjust this threshold as needed

    # Check if the eyes are closed
    if eyes_info['avg_ear'] < eye_closed_threshold:
        return True  # Eyes are closed
    else:
        return False  # Eyes are open
