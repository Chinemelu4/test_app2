import streamlit as st
import pandas as pd
from plotly import express as px

st.title("First Analytics App")

df = pd.read_csv("melbourne.csv")

st.dataframe(df)

regions = df['Regionname'].unique()

st.selectbox('Choose a region',regions)

st.selectbox('GENDER',['Male','Female'])

st.radio('Gender',['Male','Female'])

st.number_input('Enter a number',step=1)
st.text_input('Enter your name')
st.date_input('Enter your date of birth')

house_ct = df['Type'].value_counts().to_frame()

#st.dataframe(house_ct)
x = house_ct.index
y = house_ct['count']

fig1 = px.bar(x=x,y=y)

#st.plotly_chart(fig1)

fig2 = px.pie(house_ct,values='count',names=x)
#st.plotly_chart(fig2)

col1, col2 = st.columns(2) 

with col1:
    st.plotly_chart(fig1)

with col2:
    st.plotly_chart(fig2)
