# image_utils.py
import cv2
import numpy as np


def draw_bounding_box(frame, box, color=(0, 155, 255), thickness=2):
    x, y, w, h = map(int, box)
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)


def draw_landmarks(frame, landmarks, color=(0, 155, 255), radius=2):
    for point in landmarks.values():
        cv2.circle(frame, point, radius, color, -1)


def save_frame(frame, file_path):
    cv2.imwrite(file_path, frame)


def resize_frame(frame, width=None, height=None):
    if width and height:
        return cv2.resize(frame, (width, height))
    elif width:
        return cv2.resize(frame, (width, int(frame.shape[0] * width / frame.shape[1])))
    elif height:
        return cv2.resize(frame, (int(frame.shape[1] * height / frame.shape[0]), height))
    else:
        return frame


def convert_to_grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def stack_frames_horizontally(frames):
    return np.hstack(frames)


def stack_frames_vertically(frames):
    return np.vstack(frames)
