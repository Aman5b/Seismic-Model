import numpy as np
import pandas as pd
import pickle
#import matplotlib.pyplot as plt
#import seaborn as sns

import streamlit as st

pickle_in = open(r"C:\Users\Aman\Seismic Model\reg.pkl", "rb") 
magni = pickle.load(pickle_in)

#Latitude = 2.25
#Longitude = 5.89
#Hour = 14
#Date = 20
#Month = 8
#Year = 2021
#magni = pickle_in.predict([[Latitude, Longitude, Hour, Date, Month, Year]])
#print(magni)



def welcome():
    return "WELCOME ALL"

def predict_magni_depth(latitude, longitude, hour, date, month, year):
    prediction = magni.predict([[latitude, longitude, hour, date, month, year]])
    print(prediction)
    return prediction

def main():
    st.title("Seismic Insights")
    html_temp = """
    <div style=background-color:pink; padding:10px>    
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    latitude = st.number_input("Latitude")
    longitude = float(latitude)
    longitude = st.number_input("Longitude")
    longitude = float(longitude)
    hour = st.number_input("Hour (24 hour)")
    hour = int(hour)
    date = st.number_input("Date")
    date = int(date)
    month = st.number_input("Month")
    month = int(month)
    year = st.number_input("Year")
    year = int(year)
    result = ""
    if st.button("Predict"):
        result = predict_magni_depth(latitude, longitude, hour, date, month, year)
    st.success('The Output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with streamlit")

if __name__ == '__main__':
    main()
