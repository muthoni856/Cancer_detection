import os
from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the saved model
model = tf.keras.models.load_model('cancer_prediction_model.keras')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to preprocess the image
def preprocess_image(file):
    img = load_img(file, target_size=(150, 150))  # Resize the image to 150x150 pixels
    img_array = img_to_array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch size
    img_array /= 255.0  # Scale the pixel values to [0, 1]
    return img_array #this is an array of images

# Function to predict the class of the image
def predict_image(file):
    processed_image = preprocess_image(file)
    prediction = model.predict(processed_image)
    class_label = 'malignant' if prediction[0][0] > 0.5 else 'benign'
    return class_label

@app.route("/", methods=["GET", "POST"]) #points to the root directory for GET an POST requests
def form():
    result = None
    file_url = None
    #POST Method
    if request.method == "POST":
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)  # Save the file temporarily
            result = predict_image(file_path)
            os.remove(file_path)  # Clean up the saved file after prediction
    return render_template('index.html', result=result)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
