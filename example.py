import cv2
from mtcnn.mtcnn import MTCNN


def detect_faces_and_draw_boxes(image_path):
    # Initialize MTCNN
    detector = MTCNN()

    # Read the image
    frame = cv2.imread(image_path)

    if frame is None:
        print(f"Error: Unable to read image from path: {image_path}")
        return

    # Resize the image to have a height of 50 pixels
    target_height = 50
    height, width = frame.shape[:2]
    aspect_ratio = target_height / height
    target_width = int(width * aspect_ratio)
    resized_frame = cv2.resize(frame, (target_width, target_height))

    # Detect faces in the resized image
    detections = detector.detect_faces(resized_frame)

    for detection in detections:
        # Extract face coordinates
        x, y, width, height = detection['box']

        # Scale the coordinates back to the original image size
        x = int((x / target_width) * width)
        y = int((y / target_height) * height)
        width = int((width / target_width) * width)
        height = int((height / target_height) * height)

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

        # Display confidence score
        confidence = detection['confidence']
        text = f'Confidence: {confidence:.2f}'
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the image with face detection
    cv2.imshow('Face Detection', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Example usage with an image path
    image_path = "3.jpg"
    detect_faces_and_draw_boxes(image_path)
