import numpy as np
from flask import Flask, request, render_template
import pickle



app = Flask(__name__)
model = pickle.load(open('randomForestRegressor666.pkl','rb'))
    

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/predict',methods = ['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="AQI for Jaipur {}".format(output))



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)