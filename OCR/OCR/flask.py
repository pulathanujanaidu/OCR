from flask import Flask, render_template, request
import easyocr
import cv2
from matplotlib import pyplot as plt
import os

app = Flask(__name__)

# Initialize EasyOCR reader for English and Telugu languages
reader = easyocr.Reader(['en', 'te'])

# Define the path to the upload directory
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define allowed extensions for uploaded files
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


# Function to check if the file has allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', message='No file selected')

    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Read the uploaded image
        img = cv2.imread(filepath)

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

        # Save the annotated image
        annotated_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'annotated_' + filename)
        cv2.imwrite(annotated_image_path, img)

        return render_template('result.html', filename=filename, annotated_image='annotated_' + filename)

    else:
        return render_template('index.html', message='Invalid file format')


if __name__ == '__main__':
    app.run(debug=True)
