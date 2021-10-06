import streamlit as st 
import pandas as pd
from PIL import Image
import src.support as sp

st.write('''
# THE HISTORY OF SPORTS...
# Which sport is for me?

''')

st.write('''
### What can you find here?

''')
st.text(''' Here you will find awesome graphs describing 
the most profiteable sports in the last 30 years as well 
as an interactive part to know which sport suits you the best''')

st.write('''
## Let's start by exploring the difficutly of the sports we have in our study
''')

imagen1 = Image.open("images/histogram.png")
st.image(imagen1, use_column_width=True)

st.plotly_chart(sp.all_sports())

st.write('''
## Now we will dive a little bit into the money earned by the top sports in the last 30 years
''')

st.plotly_chart(sp.sum_earnings())

st.text('''But...how has each top sport changed in the last 30 years?''')

st.plotly_chart(sp.change_sports())

st.text('''And... how much are this sports going to raise in the next 10 years?''')

col1, col2 = st.columns(2)
with col1:
    imagen = Image.open("images/graph_golf.png")
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open("images/graph_soccer.png")
    st.image(imagen, use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    imagen = Image.open("images/graph_auto_racing.png")
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open("images/graph_boxing.png")
    st.image(imagen, use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    imagen = Image.open("images/graph_football.png")
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open("images/graph_tennis.png")
    st.image(imagen, use_column_width=True)

    imagen = Image.open("images/graph_baseball.png")
    st.image(imagen, use_column_width=True)

st.write('''
## It may be interesting to know how the 10 abilities are spread out throughout our top sports
''')
st.plotly_chart(sp.abilities_xsports())

st.write('''
## For the same reason we want to look at pur top sports individually to observe its abilities
''')

st.plotly_chart(sp.sports_xabilities())

st.write('''
## Clustering the sports is interesting for understanding some common characteristics
''')

imagen= Image.open("images/clusters.png")
st.image(imagen, use_column_width=True)

st.sidebar.header('Enter the score you give to yourself for each skill')

df = sp.user_input()
st.subheader('Your skills')
st.table(df)