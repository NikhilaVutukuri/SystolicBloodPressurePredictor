from flask import Flask,request,render_template
import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('website.html')

@app.route('/predict',methods=['GET','POST'])
def my_form_post():
    if request.method=='POST':
        age=request.form['age']
        weight=request.form['weight']
        clf = joblib.load("/home/NikhilaVutukuri/mysite/regr.pkl")
        x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
        bloodpressure = clf.predict(x)[0]
    return render_template('website.html',bloodpressure=bloodpressure)
