import dlib
from Eye_Detection.eye_detection import eye_aspect_ratio


def detect_baby_eyes(frame, keypoints):
    # Check if 'left_eye' and 'right_eye' keys are present in the keypoints dictionary
    if 'left_eye' in keypoints and 'right_eye' in keypoints:
        # Extract bounding box from MTCNN detection
        box = keypoints['box']
        x, y, w, h = box

        # Extract region of interest (ROI) from the frame using the bounding box
        face_roi = frame[y:y+h, x:x+w]

        # Initialize dlib's face detector
        face_detector = dlib.get_frontal_face_detector()

        # Detect faces in the ROI using dlib
        dlib_detections = face_detector(face_roi)

        if len(dlib_detections) > 0:
            # Assume the first face detection is the correct one (you may need to handle multiple detections differently)
            landmarks = dlib_detections[0]

            # Calculate EAR for each eye using dlib landmarks
            left_eye = [(landmarks.part(i).x, landmarks.part(i).y)
                        for i in range(36, 42)]
            right_eye = [(landmarks.part(i).x, landmarks.part(i).y)
                         for i in range(42, 48)]

            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)

            # Average EAR of both eyes
            avg_ear = (left_ear + right_ear) / 2.0

            return {'left_ear': left_ear, 'right_ear': right_ear, 'avg_ear': avg_ear}
    else:
        # If 'left_eye' or 'right_eye' is not present, return a default value or handle accordingly
        return {'left_ear': 0, 'right_ear': 0, 'avg_ear': 0}
