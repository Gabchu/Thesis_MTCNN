# from mtcnn import MTCNN
# import os
# import cv2
# import shutil


# def evaluate_face_detection(model, test_folder, label, output_folder):
#     correct_predictions = 0
#     total_images = 0

#     # Create output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     for filename in os.listdir(test_folder):
#         if filename.endswith(".jpg") or filename.endswith(".png"):
#             image_path = os.path.join(test_folder, filename)
#             img = cv2.imread(image_path)
#             result = model.detect_faces(img)

#             # If faces are detected (positive) or not (negative)
#             if (result and len(result) > 0 and label == "positive") or (not result and label == "negative"):
#                 correct_predictions += 1
#             else:
#                 # Save wrongly predicted images to the output folder
#                 output_path = os.path.join(output_folder, filename)
#                 shutil.copy2(image_path, output_path)

#             total_images += 1

#     if total_images > 0:
#         accuracy = correct_predictions / total_images
#         print(f"Accuracy for {label} images: {accuracy:.2%}")
#         print(f"Wrongly predicted images saved in: {output_folder}")
#     else:
#         print(f"No valid images found in the {label} test folder.")


# # Path to the test dataset folders
# positive_test_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\phone"
# negative_test_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\test\negative"

# # Output folders for wrongly predicted images
# positive_output_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\output\wrongly_predicted_positive"
# negative_output_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\output\wrongly_predicted_negative"

# # Create MTCNN model
# mtcnn_model = MTCNN()

# # Evaluate face detection on positive test images
# evaluate_face_detection(mtcnn_model, positive_test_folder,
#                         label="positive", output_folder=positive_output_folder)

# # Evaluate face detection on negative test images
# evaluate_face_detection(mtcnn_model, negative_test_folder,
#                         label="negative", output_folder=negative_output_folder)

# from mtcnn import MTCNN
# import os
# import cv2


# def evaluate_face_detection(model, test_folder):
#     correct_predictions = 0
#     total_images = 0

#     for filename in os.listdir(test_folder):
#         if filename.endswith(".JPG") or filename.endswith(".PNG"):
#             image_path = os.path.join(test_folder, filename)
#             img = cv2.imread(image_path)
#             result = model.detect_faces(img)

#             # If faces are detected (positive) or not (negative)
#             if (result and len(result) > 0) or (not result):
#                 correct_predictions += 1

#             total_images += 1

#     if total_images > 0:
#         accuracy = correct_predictions / total_images
#         print(f"Overall accuracy: {accuracy:.2%}")
#     else:
#         print("No valid images found in the test folder.")


# # Path to the test dataset folder
# test_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\phone"

# # Create MTCNN model
# mtcnn_model = MTCNN()

# # Evaluate face detection on test images
# evaluate_face_detection(mtcnn_model, test_folder)

from mtcnn import MTCNN
import os
import cv2
import shutil


def evaluate_face_detection(model, test_folder, label, output_folder):
    correct_predictions = 0
    total_images = 0

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(test_folder):
        if filename.endswith(".JPG") or filename.endswith(".png"):
            image_path = os.path.join(test_folder, filename)
            img = cv2.imread(image_path)
            result = model.detect_faces(img)

            # If faces are detected (positive)
            if result and len(result) > 0 and label == "positive":
                correct_predictions += 1
            else:
                # Save wrongly predicted images to the output folder
                output_path = os.path.join(output_folder, filename)
                shutil.copy2(image_path, output_path)

            total_images += 1

    if total_images > 0:
        accuracy = correct_predictions / total_images
        print(f"Accuracy for {label} images: {accuracy:.2%}")
        print(f"Wrongly predicted images saved in: {output_folder}")
    else:
        print(f"No valid images found in the {label} test folder.")


# Path to the test dataset folder
positive_test_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\phone"

# Output folder for wrongly predicted images
positive_output_folder = r"C:\Users\terre\OneDrive\Desktop\Project_MTCNN\output\wrongly_predicted_positive"

# Create MTCNN model
mtcnn_model = MTCNN()

# Evaluate face detection on positive test images
evaluate_face_detection(mtcnn_model, positive_test_folder,
                        label="positive", output_folder=positive_output_folder)
