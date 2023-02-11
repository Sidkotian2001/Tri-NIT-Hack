from flask import Flask,request,jsonify
import joblib
import numpy as np
import datetime
import pandas as pd
app = Flask(__name__)

model=joblib.load('my_random_forest.joblib')

@app.route('/')
def home():
    return "Hello"

# 

def get_temp_rainfall(state,harvest_month):
    df_ = pd.read_csv('Predict.csv')
    closest_city = {
    "Andhra Pradesh": "Chennai",
    "Arunachal Pradesh": None,
    "Assam": None,
    "Bihar": None,
    "Chhattisgarh": None,
    "Goa": "Mumbai",
    "Gujarat": "Mumbai",
    "Haryana": "Delhi",
    "Himachal Pradesh": None,
    "Jharkhand": None,
    "Karnataka": "Bangalore",
    "Kerala": "Chennai",
    "Madhya Pradesh": None,
    "Maharashtra": "Mumbai",
    "Manipur": None,
    "Meghalaya": None,
    "Mizoram": None,
    "Nagaland": None,
    "Odisha": None,
    "Punjab": "Delhi",
    "Rajasthan": "Delhi",
    "Sikkim": None,
    "Tamil Nadu": "Chennai",
    "Telangana": None,
    "Tripura": None,
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": None,
    "West Bengal": None
    }

    

    city = closest_city[state]
    print(city)

    df_ = df_[df_['city']==city]
    current_month = datetime.datetime.now().month
    # now between those months take the average
    print(harvest_month)
    df_ = df_[(df_['month']>=current_month) & (df_['month']<=harvest_month)]
    prcp = df_['prcp'].mean()
    tavg = df_['tavg'].mean()
    print(tavg,prcp)
    return tavg,prcp

@app.route('/predict',methods=['POST'])
def predict():

    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }

    nitrogen=int(request.form.get('nitrogen'))
    phosphorus=int(request.form.get('phosphorus'))
    potassium=int(request.form.get('potassium'))
    loca=request.form.get('location')
    ph=int(request.form.get('ph'))
    mont=request.form.get('month')

    rainfall,temp = get_temp_rainfall(loca,months[mont])
    input_query = np.array([[nitrogen,phosphorus,potassium,temp,ph,rainfall]])
    prob=model.predict_proba(input_query)
    top=np.argsort(-prob, axis=1)[:, :8]
    count=1
    res={}
    for i in top[0]:
        res[count]=model.classes_[i]
        count=count+1
    return jsonify(res)


if __name__=='__main__':
    app.run()
