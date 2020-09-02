# Dog or cat predictor

This is a simple Flask app to predict if an image is a cat or a dog.
The predictor model is based on a convoluted neural network built using keras in tensorflow.

The model took 48 hours to train. The accuracy was 98%.

To try it on the web visit:  
https://dogcatpredictor.herokuapp.com/  

To run the app locally:

git clone git@github.com:dr-robin/dogcatpredictor.git  
cd ./dogcatpredictor  
export FLASK_APP=app.py  
flask run  
Open a browser at http://127.0.0.1:5000/   

# Credits

The excellent documentation and tutorials provided by Keras and Tensorflow
https://keras.io/getting_started/intro_to_keras_for_engineers/  
https://www.tensorflow.org/api_docs
