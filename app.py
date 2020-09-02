import os
from flask import Flask, render_template, request, send_from_directory
import numpy as np
import tensorflow as tf
#from tensorflow import keras
from tensorflow.keras.models import load_model

import numpy as np
import os

app = Flask(__name__)

STATIC_FOLDER = 'static'
# Path to the folder to store uploaded image
UPLOAD_FOLDER = STATIC_FOLDER + '/uploads'
# Path to the folder with model.h5
MODEL_FOLDER = STATIC_FOLDER + '/models'

def predict(fullpath):
    #Load saved model.h5
    model = load_model(MODEL_FOLDER + '/model.h5')
    #Load image
    test_image = tf.keras.preprocessing.image.load_img(fullpath, target_size=(180, 180, 3))
    test_image = np.expand_dims(test_image, axis=0)
    # Scale image
    test_image = test_image.astype('float') / 255  #may need .flatten()
    # Predict image label using model
    result = model.predict(test_image) #may need .flatten()
    return result


#Landing page
@app.route('/')
def index():
    return render_template('index.html')


# Process image and predict label
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['image']
        fullname = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(fullname)

        result = predict(fullname)

        pred_prob = result.item()

        if pred_prob > .5:
            label = 'Dog'
            accuracy = round(pred_prob * 100, 2)
        else:
            label = 'Cat'
            accuracy = round((1 - pred_prob) * 100, 2)

        return render_template('predict.html', image_file_name=file.filename, label=label, accuracy=accuracy)


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


def create_app():
    load__model()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
