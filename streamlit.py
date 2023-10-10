import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
st.title("Car Prices Dataset")
st.write("This dataset provides a comprehensive collection of specifications and pricing details for a diverse range of cars. It serves as a valuable resource for automotive enthusiasts, researchers, and industry professionals looking to analyze and understand the intricate relationships between various car attributes and their market prices.")
def load_data(nrows):
    data = pd.read_csv("carprices.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data...done!')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
data['torque (lb-ft)'] = pd.to_numeric(data['torque (lb-ft)'], errors='coerce')
data['engine size (l)'] = pd.to_numeric(data['engine size (l)'], errors='coerce')
data.dropna(subset=['torque (lb-ft)', 'engine size (l)'], inplace=True)
st.write("""This bar chart below represents the performance of different car models based on their torque values. 
Torque is a measure of the force that can cause an object to rotate about an axis. 
In the context of cars, it indicates the power of the engine and its ability to do work.""")
min_torque, max_torque = int(data['torque (lb-ft)'].min()), int(data['torque (lb-ft)'].max())
torque_range = st.slider("Select Torque Range", min_torque, max_torque, (min_torque, max_torque))
filtered_data = data[(data['torque (lb-ft)'] >= torque_range[0]) & (data['torque (lb-ft)'] <= torque_range[1])]
fig = px.bar(filtered_data, x="car model", y='torque (lb-ft)')
st.subheader(f"Bar Chart for Cars with Torque between {torque_range[0]} and {torque_range[1]} lb-ft")
st.plotly_chart(fig)
st.write("""This box plot below visualizes the distribution of car prices for different car makes. 
The box represents the interquartile range (IQR), showing the middle 50% of the data. 
The whiskers extend to the minimum and maximum values within 1.5 times the IQR. 
Outliers may be plotted as individual points outside the whiskers.""")
selected_make = st.selectbox("Select Car Make", data['car make'].unique())
filtered_data_make = data[data['car make'] == selected_make]
fig1 = px.box(filtered_data_make, x="car make", y="price (in usd)")
st.subheader(f"Price of {selected_make} Cars")
st.plotly_chart(fig1)
st.write("""This histogram below displays the frequency distribution of engine sizes for the cars in the dataset. 
The x-axis represents different engine sizes (in liters), while the y-axis shows the number of cars 
that fall within each engine size range. This visualization helps understand the most common engine sizes 
in the dataset.""")
min_engine, max_engine = float(data['engine size (l)'].min()), float(data['engine size (l)'].max())
engine_range = st.slider("Select Engine Size Range", min_engine, max_engine, (min_engine, max_engine))
filtered_data_engine = data[(data['engine size (l)'] >= engine_range[0]) & (data['engine size (l)'] <= engine_range[1])]
fig2 = px.histogram(filtered_data_engine, x='engine size (l)')
st.subheader(f"Frequency of Cars with Engine Size between {engine_range[0]} and {engine_range[1]} L")
st.plotly_chart(fig2)
