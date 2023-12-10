from scipy.spatial import distance as dist


def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


def detect_eyes(frame, landmarks):
    # Extract coordinates for left eye landmarks (example assumes dlib's numbering convention)
    left_eye = [landmarks.part(i).x for i in range(36, 42)], [
        landmarks.part(i).y for i in range(36, 42)]

    # Extract coordinates for right eye landmarks (example assumes dlib's numbering convention)
    right_eye = [landmarks.part(i).x for i in range(42, 48)], [
        landmarks.part(i).y for i in range(42, 48)]

    # Calculate EAR for each eye
    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    # Average EAR of both eyes
    avg_ear = (left_ear + right_ear) / 2.0

    return {'left_ear': left_ear, 'right_ear': right_ear, 'avg_ear': avg_ear}
