import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(float(x)) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)
    if prediction < 0.5 :
        result="Good News! You do not have Diabetes!"
    else :
        result="There is a high chance of you having diabetes."
    print(prediction)
    return render_template('index.html', prediction_text='{}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)