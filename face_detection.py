# face_detection.py
import dlib
import cv2


def detect_face(frame):
    # If enough time has passed, perform face detection
    hog_face_detector = dlib.get_frontal_face_detector()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection using dlib
    detections = hog_face_detector(gray_frame)

    for det in detections:
        # Extract bounding box coordinates
        x1, y1, x2, y2 = det.left(), det.top(), det.right(), det.bottom()
        for k, d in enumerate(detections):
            cv2.rectangle(frame, (d.left(), d.top()),
                          (d.right(), d.bottom()), (255, 0, 255), 2)
        # Extract facial landmarks (you may need to adjust based on your use case)
        shape = predictor(gray_frame, det)
        keypoints = {
            'box': (x1, y1, x2, y2),
            'left_eye': (shape.part(36).x, shape.part(36).y),
            'right_eye': (shape.part(45).x, shape.part(45).y),
            # Add more landmarks as needed
        }

        return keypoints

    return None


predictor_path = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
