# camera.py
import cv2


def start_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    cap.set(cv2.CAP_PROP_FPS, 10)

    return cap


def display_frame(window_name, frame):
    cv2.imshow(window_name, frame)


def wait_key(delay):
    return cv2.waitKey(delay)


def release_resources(cap):
    cap.release()
    cv2.destroyAllWindows()
