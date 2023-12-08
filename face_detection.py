# face_detection.py
from mtcnn import MTCNN


def detect_face(frame):
    detector = MTCNN()
    detections = detector.detect_faces(frame)

    min_conf = 0.9
    confidence_score = 0  # Initialize confidence score

    for det in detections:
        if det['confidence'] >= min_conf:
            keypoints = det['keypoints']
            confidence_score = det['confidence']  # Extract confidence score
            return {'box': det['box'], 'keypoints': keypoints}, confidence_score

    return None, confidence_score
