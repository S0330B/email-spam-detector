import pandas as pd
import streamlit as st
import joblib

pipe = joblib.load('multinomial_nb.joblib')  

st.title("Email Spam Detector")

message = st.text_area("Enter the Email Message:")

if st.button("Predict"):
    if message.strip() == "":
        st.info("Please enter an email message to predict.")
    else:
        prediction = pipe.predict([message])
        if prediction[0] == 1:
            st.error("This is a spam email.")
        else:
            st.success("This is not a spam email.")
