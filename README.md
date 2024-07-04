
Here's the README file in plain Markdown format:

---

# Skin Cancer Classification

This project is a web application for detecting skin cancer from uploaded images. It uses a pre-trained TensorFlow model to classify images as either benign or malignant. The web interface allows users to upload an image and receive a prediction result.

## Project Structure


.
├── static
│   ├── backcancer.jpg
│   └── backcancer2.jpg
├── templates
│   └── index.html
├── uploads
├── app.py
└── cancer_prediction_model.keras


- *static/*: Directory for storing static files like images.
  - backcancer.jpg: Background image used in the web interface.
  - backcancer2.jpg: Background image used in the web interface.
- *templates/index.html*: The HTML template for the web interface.
- *uploads/*: Directory for storing uploaded images temporarily.
- *app.py*: The main Flask application file.
- *cancer_prediction_model.keras*: The pre-trained TensorFlow model for skin cancer prediction.

## Prerequisites

- Python 3.12.4
- Flask
- TensorFlow
- Werkzeug

## Installation

1. Clone the repository:
    bash
    git clone https://github.com/yourusername/skincancer-classification.git
    cd skincancer-classification
    

2. Create a virtual environment and activate it:
    bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

3. Install the required packages:
    bash
    pip install flask tensorflow werkzeug
    

4. Ensure the uploads directory exists:
    bash
    mkdir -p uploads
    

## Usage

1. Start the Flask application:
    bash
    python app.py
    

2. Open your web browser and go to http://127.0.0.1:5000/.

3. Use the web interface to upload an image of skin and click "Upload and Predict".

4. The application will display the prediction result as either "benign" or "malignant".

## Project Details

### index.html

The HTML file provides a simple form for users to upload an image. It includes a CSS section for styling and a form that posts the image file to the server for prediction.

### app.py

The Flask application:
- Loads the pre-trained model.
- Defines routes and functions for handling file uploads and predictions.
- Processes images by resizing them and scaling pixel values.
- Makes predictions using the TensorFlow model.

### cancer_prediction_model.keras

This file contains the saved TensorFlow model used for predicting skin cancer.

### static/backcancer.jpg and static/backcancer2.jpg

These are background images used in the web interface for aesthetic purposes.

## License

This project is licensed under the MIT License.

---
