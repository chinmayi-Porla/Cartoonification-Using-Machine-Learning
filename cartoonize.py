from flask import Flask, render_template, request, redirect, flash
import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import os
import base64

# Create the static directory if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    return render_template('index.html')

def process_image(img):
    #img = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    # Image processing (cartoonize) code
    line_size = 7
    blur_value = 7

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray_img, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)

    k = 7
    data = img.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, random_state=42).fit(data)
    img_reduced = kmeans.cluster_centers_[kmeans.labels_]
    img_reduced = img_reduced.reshape(img.shape)
    img_reduced = img_reduced.astype(np.uint8)
    blurred = cv2.bilateralFilter(img_reduced, d=7, sigmaColor=200, sigmaSpace=200)
    cartoon_img = cv2.bitwise_and(blurred, blurred, mask=edges)
    return cartoon_img

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle the POST request to process the uploaded image
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        img = Image.open(file.stream)
        img.save('static/uploaded_image.png')  # Save the uploaded image

        # Convert PIL image to OpenCV format
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Process the image
        processed_img = process_image(img)

        # Save the processed image
        cv2.imwrite('static/cartoonized_image.png', processed_img)

        return redirect('/result')  # Redirect to the result page after processing

    # Render the upload form for GET requests
    return render_template('upload.html')

@app.route('/result')
def result():
    uploaded_path = 'static/uploaded_image.png'
    cartoon_path = 'static/cartoonized_image.png'

    return render_template('result.html', uploaded_path=uploaded_path, cartoon_path=cartoon_path)

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/process_webcam_image', methods=['POST'])
def process_webcam_image():
    data = request.json
    img_data = base64.b64decode(data['image'].split(',')[1])  # Extract base64 image data
    nparr = np.frombuffer(img_data, np.uint8)  # Convert bytes to numpy array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Decode image
    processed_img = process_image(img)  # Process the image

    # Save the captured image
    captured_path = 'static/uploaded_image.png'
    cv2.imwrite(captured_path, img)

    # Save the processed image
    processed_path = 'static/cartoonized_image.png'
    cv2.imwrite(processed_path, processed_img)

    return redirect('/result')

if __name__ == '__main__':
    app.run(debug=True)