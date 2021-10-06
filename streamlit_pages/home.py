import streamlit as st 
import pandas as pd
from PIL import Image
import src.support as sp


def app():

    st.write('''
    ## What can you find here?

    ''')
    st.text(''' 
    Here you will find awesome graphs describing 
    the most profiteable sports in the last 30 years as well 
    as an interactive part to know which sport suits you the best''')

    imagen = Image.open("images/awesome meme.jpg")
    st.image(imagen, use_column_width=True)
