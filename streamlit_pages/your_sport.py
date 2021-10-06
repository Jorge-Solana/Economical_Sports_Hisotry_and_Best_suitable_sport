import streamlit as st 
import pandas as pd
from PIL import Image
import src.support as sp


def app():
    imagen = Image.open("images/prediction meme.jpg")
    st.image(imagen, use_column_width=True)




    st.sidebar.header('Enter the score you give to yourself for each skill')

    df = sp.user_input()
    st.subheader('Your skills')
    st.table(df)

    st.text(''' Based on your abilities....''')
    st.text(sp.give_sport(df))