import streamlit as st

creditcard= st.number_input("What is your Credit Card number")
date_exp = st.number_input("Date of Expiration")
user = st.number_input("Name of card holder")
ssn = st.number_input(" Social Security Number")

submit = st.button("Submit")
if submit:
    st.write("GET Scammed BITCH")
