import cv2
from mtcnn.mtcnn import MTCNN

# Initialize MTCNN
detector = MTCNN()

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Detect faces in the frame
    detections = detector.detect_faces(frame)

    for detection in detections:
        # Extract face coordinates
        x, y, width, height = detection['box']

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

        # Display confidence score
        confidence = detection['confidence']
        cv2.putText(frame, f'Confidence: {confidence:.2f}', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
