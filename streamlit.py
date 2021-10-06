import streamlit as st 
import pandas as pd
from PIL import Image
import src.support as sp
from multipage import MultiPage
from streamlit_pages import home
from streamlit_pages import graphs
from streamlit_pages import your_sport




app = MultiPage()

st.title('THE STORY OF SPORTS... Which one is for me?')

app.add_page('Home', home.app)
app.add_page('Graphs', graphs.app)
app.add_page('Your sport', your_sport.app)



app.run()

