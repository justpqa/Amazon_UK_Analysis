import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv(".env.tableau")

def show_tableau_graph(sheet_name, w, h):
    sheet = os.environ["TABLEAU_LINK"].format(sheet = sheet_name)
    st.components.v1.iframe(sheet, width = w, height = h)

def sidebar_setup():
    with st.sidebar:
        st.page_link('Welcome.py', label='Welcome')
        st.page_link('pages/Stars_Rating_Analysis.py', label='1. Analysis of Stars Rating')
        st.page_link('pages/Notable_categories.py', label='2. Notable product categories')
        st.page_link('pages/Most_bought_categories_analysis.py', label='3. Analysis of most bought categories')
        st.page_link('pages/Unique_most_bought_category.py', label='4. A unique most bought categories')
        st.page_link('pages/Naming_of_top_products.py', label='5. Naming of top products')