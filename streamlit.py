import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
st.title("Car Prices Dataset")
st.write("This dataset provides a comprehensive collection of specifications and pricing details for a diverse range of cars. It serves as a valuable resource for automotive enthusiasts, researchers, and industry professionals looking to analyze and understand the intricate relationships between various car attributes and their market prices.")
def load_data(nrows):
    data = pd.read_csv("C:/Users/dell/OneDrive/Desktop/MSBA 325/carprices.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data...done!')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
st.subheader("Bar Chart for Performance of Cars")
fig = px.bar(data,x="car model",y='torque (lb-ft)')
st.plotly_chart(fig)
st.subheader("Price of Cars")
df = data.sort_values(by='price (in usd)', ascending = False)
fig1 = px.box(df,x="car make",y="price (in usd)")
st.plotly_chart(fig1)
st.subheader("Frequency of Engine Size")
fig2  = px.histogram(data,x= 'engine size (l)')
st.plotly_chart(fig2)