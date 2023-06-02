import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.applications.ResNet50(weights='imagenet')

def preprocess_image(image):
    image = image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

def predict_car_brand(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    results = tf.keras.applications.resnet50.decode_predictions(predictions, top=5)[0]
    for result in results:
        print(f"{result[1]}: {result[2] * 100}%")

image_path = "supra.jpg"
image = Image.open(image_path)

predict_car_brand(image)