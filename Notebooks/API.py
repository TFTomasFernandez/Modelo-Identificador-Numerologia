from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('my_mnist_model.h5')

@app.route('/')
def home():
    return "Welcome to the MNIST Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    image = np.array(data['image'])
    image = image.reshape((1, 28, 28))  # Asegúrate de que la imagen esté en el formato correcto
    prediction = model.predict(image)
    predicted_label = np.argmax(prediction[0])
    return jsonify({'prediction': int(predicted_label)})

if __name__ == '__main__':
    app.run(debug=True)
