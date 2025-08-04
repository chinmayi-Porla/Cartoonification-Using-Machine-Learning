

```markdown
# 🎨 Cartoonify: AI-Powered Image Transformation

This project transforms normal images and webcam videos into cartoon-style visuals using image processing and basic machine learning techniques. The aim is to apply a creative and engaging visual transformation using computer vision, suitable for social media filters, mobile applications, and creative editing tools.



## 📌 Project Description

Cartoonification is the process of converting a real-world image into a cartoon-style representation by simplifying the color palette, enhancing edges, and reducing image complexity.

This project leverages:
- Image processing techniques using **OpenCV**
- A simple yet effective **Python + HTML web interface**
- Optionally integrates webcam support for **real-time cartoon effects**



## 🧠 Techniques Used

### 📷 Image Processing Workflow:
The cartoon effect is generated using the following steps:
1. **Read Image**: Load the image using OpenCV.
2. **Grayscale Conversion**: Convert the image to grayscale.
3. **Noise Reduction**: Apply a bilateral filter to remove noise while preserving edges.
4. **Edge Detection**: Use adaptive thresholding to highlight edges.
5. **Color Filtering**: Use bilateral filter on the original image to flatten the color regions.
6. **Combining**: Merge the edge mask with the smoothed color image to produce the cartoon effect.


## 🗂️ Project Structure

```

Cartoonification-Using-Machine-Learning/
│
├── cartoon.ipynb            # Jupyter notebook demonstrating cartoonification
├── cartoonize.py            # Python script for cartoonifying images
│
├── index.html               # Main HTML upload form
├── upload.html              # Image upload interface
├── result.html              # Displays cartoonified result
├── webcam.html              # Real-time cartoonification using webcam
│
└── README.md                # Project overview

````



## 🌐 Web Application Overview

This project includes a lightweight HTML interface to allow users to interact with the cartoonifier:

- **`index.html`** – Landing page with buttons to upload images or access the webcam.
- **`upload.html`** – Form where users upload their image for processing.
- **`result.html`** – Displays the final cartoonified version.
- **`webcam.html`** – Captures webcam feed and applies cartoon filters in real time.



## ⚙️ How to Use

### 🔧 Prerequisites

Install the required Python packages:

```bash
pip install opencv-python numpy flask matplotlib
````



### 🖼️ Run with Python

1. Save an image (e.g., `input.jpg`) in your working directory.
2. Run the script:

```bash
python cartoonize.py --image input.jpg
```

3. The output will be saved and displayed as a cartoonified image.



### 📓 Run via Notebook

1. Open `cartoon.ipynb` in Jupyter Notebook or Google Colab.
2. Upload your image when prompted.
3. Run the notebook cells to view the cartoonified output.

---

### 🌍 Run Web Interface (Optional Flask Integration)

If you want to integrate this with a Flask server:

```bash
from flask import Flask, render_template, request
# ... (Flask code to render HTML, accept images, and return results)
```

> Note: The HTML pages are static in the project, but they can be integrated into a Flask app to make it fully functional.


## 📽️ Webcam Cartoonification

1. Open `webcam.html` in your browser.
2. Grant webcam access.
3. The video stream will be cartoonified in real-time using the pre-defined script.



## 📷 Example Output

Original Image ➡️ Cartoonified Output

*(You can add screenshots here when deploying on GitHub or in your presentation)*



## ✅ Features

* Converts any image to cartoon style
* Simple user interface via web forms
* Real-time webcam cartoon filter (HTML based)
* Jupyter Notebook for demonstration
* Lightweight, no GPU or heavy ML models required



## 🚀 Future Enhancements

* Integrate with Flask backend for dynamic file uploads
* Apply deep learning-based image stylization (e.g., CycleGAN, U-Net)
* Add support for batch image processing
* Extend real-time video processing with OpenCV



## 🙋‍♂️ Author

Developed as part of a creative computer vision project on image transformation using Python.


## 📄 License

This project is open-source under the MIT License. Feel free to modify and use it for personal or educational purposes.

```


