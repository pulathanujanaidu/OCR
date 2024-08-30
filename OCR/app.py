import easyocr
import cv2
from matplotlib import pyplot as plt

IMAGE_PATH = 'html.jpg'

# Initialize EasyOCR reader for English ,telugu language,hindi language
reader = easyocr.Reader(['en', 'te'])


# Read the image
img = cv2.imread(IMAGE_PATH)

# Perform OCR on the entire image
results = reader.readtext(img)

# Loop through the results and print the detected text
for (bbox, text, prob) in results:
    print(text)
    # Extract bounding box coordinates
    (top_left, top_right, bottom_right, bottom_left) = bbox
    # Convert coordinates to integers
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    # Draw a rectangle around the detected text
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    # Add the recognized text to the image
    cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

# Display the annotated image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()