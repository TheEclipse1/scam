import streamlit as st

creditcard= st.text_input("What is your Credit Card number")
date_exp = st.text_input("Date of Expiration")
user = st.text_input("Name of card holder")
ssn = st.text_input(" Social Secuirty Number")

submit = st.button("Submit")
if submit:
    st.write("GET Scammed BITCH")
