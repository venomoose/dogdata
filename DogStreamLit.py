import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2017.csv')
st.set_page_config(page_title = 'Dog Breeds', layout = 'wide')

st.title('Streamlit Demo Using Dog Breed Data Set')
st.write(df)

