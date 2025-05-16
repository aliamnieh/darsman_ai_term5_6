# Streamlit
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd

st.set_page_config(page_title="مدل یادگیری ماشین شما", layout="centered")

def run():
    X_train=pd.read_csv("C:\\Users\\K1\\Desktop\\python HomeWork\\term 5\\تمرین 6\\Exercises 4\\data\\X_train_for_scaling.csv")
    sc=StandardScaler()
    X_train=sc.fit_transform(X_train)

    with open("C:\\Users\\K1\\Desktop\\python HomeWork\\term 5\\تمرین 6\\Exercises 4\\model\\model.pkl",'rb') as file1:
        model=pickle.load(file1)

    with st.form(key='my_form'):
        st.title('Fraud Detecter')
        daily_tranaction_count=st.slider(label='Daily Transaction Count',min_value=0,max_value=20,step=1)
        failed_transaction_count_7d=st.slider(label='Failed Transaction Count 7d',min_value=0,max_value=20,step=1)
        account_balance=st.slider(label='Account Balance',min_value=0.0,max_value=100000.0,step=0.01)
        risk_score=st.slider(label='Risk Score',min_value=0.0,max_value=1.0,step=0.01)
        transaction_hour=st.slider(label='Transaction Hour',min_value=0,max_value=23,step=1)
        card_age=st.slider(label='Card Age',min_value=1,max_value=300,step=1)
        classify=st.form_submit_button('Classify')
        failed_tranaction_rate=(failed_transaction_count_7d/7)/daily_tranaction_count

    if classify:
        scaled_data=sc.transform([[failed_tranaction_rate,account_balance,risk_score,transaction_hour,card_age]])
        result=model.predict(scaled_data)
        if result==1:
            st.warning('Fraud Detected')
        else:
            st.success('No Fraud')