import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os
import joblib
import datetime

MSP_price = {
    'Rice' : 2040,
    'Maize' : 1962,
    'Lentil' : 6000,
    'Gram' : 5230,
    'Jute' : 4750,
    'Cocunut' : 2860,
    'Cotton' : 6080,
    'coffee' : 3400,
}


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
    if city is None:
        return None
    df_ = df_[df_['city']==city]
    current_month = datetime.datetime.now().month
    #now between those months take the average
    df_ = df_[(df_['month']>=current_month) & (df_['month']<=harvest_month)]
    prcp = df_['prcp'].mean()
    tavg = df_['tavg'].mean()
    return prcp,tavg


    
def find_yield(state_name, season, crop, farm_size):
    df = pd.read_csv('avg_yield.csv')
    df['Season'] = df['Season'].str.strip()
    matching_row = df.loc[(df['Crop'] == crop)
                        & (df['Season'] == season)]

    if matching_row.empty:
        print("No matching rows found")
    else:
        matching_row = matching_row.index[0]
        yield_value = df.loc[matching_row, 'Yield']
        print("The yield per unit area : {}".format(yield_value))
    
        total_produce = farm_size * yield_value
        cost = total_produce * MSP_price[crop]
        print("The approximate selling price is : {}".format(cost))
    
def predict_crop(N, P, K, temperature, ph, rainfall):
    mod = joblib.load('my_randoms_forest.joblib')
    X = np.array([N, P, K, temperature, ph, rainfall]).reshape(1, -1)
    y_pred = mod.predict(X)
    print("The predicted crop is : {}".format(y_pred[0]))
    return y_pred[0]
    
    



        
       
def main():
    # N = int(input("Enter the Nitrogen content: "))
    # P = int(input("Enter the Phosphorus content: "))
    # K = int(input("Enter the Potassium content: "))
    # ph = float(input("Enter the ph: "))
    # state = input("Enter the state: ")
    # harvest_month = int(input("Enter the harvest month: "))
    # data = np.array([[104,18, 30, 23.603016, 6.7, 140.91]])

    N = 104
    P= 18
    K = 30
    ph= 6.7
    state = 'Maharashtra'
    harvest_month = 10

    rainfall, temperature = get_temp_rainfall(state, harvest_month)
    print("The rainfall is : {}".format(rainfall))
    print("The temperature is : {}".format(temperature))
    if rainfall is None or temperature is None:
        print("Sorry, we don't have data for this state")
        return

    c_ = predict_crop(N, P, K, temperature, ph, rainfall)
    find_yield(state, 'Whole Year', c_, 100)

if __name__ == '__main__':
    main()