# eye_detection_function.py
import cv2
import dlib
from scipy.spatial import distance as dist
from face_detection import detect_face
import time  # Import the time module

# Function to detect baby's eyes using dlib


def detect_baby_eyes(frame):
    # Perform face detection using dlib
    faces = detect_face(frame)

    # Check if at least one face is detected
    if faces:
        # Extract region of interest (ROI) from the frame using the bounding box
        x, y, w, h = faces['box']
        face_roi = frame[y:y + h, x:x + w]

        # Initialize dlib's face detector and shape predictor
        p = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\shape_predictor_68_face_landmarks.dat"
        face_detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(p)

        # Convert the face_roi to grayscale for dlib
        gray_face_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale ROI using dlib
        dlib_detections = face_detector(gray_face_roi)

        if dlib_detections:
            # Assume the first face detection is the correct one
            landmarks = predictor(gray_face_roi, dlib_detections[0])

            # Calculate EAR for each eye using dlib landmarks
            left_eye_landmarks = [
                (landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
            right_eye_landmarks = [
                (landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

            # Calculate EAR for each eye using your formula
            left_ear = calculate_ear(left_eye_landmarks)
            right_ear = calculate_ear(right_eye_landmarks)

            # Check if eyes are opened based on your criteria
            # Adjust the threshold accordingly
            eyes_opened = left_ear > 0.2 and right_ear > 0.2

            # Introduce a 2-second delay
            time.sleep(1)

            print("Eyes Opened:", eyes_opened)

# Function to calculate EAR


def calculate_ear(eye_landmarks):
    # Calculate EAR using your formula
    A = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
    B = dist.euclidean(eye_landmarks[2], eye_landmarks[4])
    C = dist.euclidean(eye_landmarks[0], eye_landmarks[3])
    ear = (A + B) / (2.0 * C)
    return ear
