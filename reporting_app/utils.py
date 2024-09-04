import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv(".env.tableau")

def show_tableau_graph(sheet_name, w, h):
    sheet = os.environ["TABLEAU_LINK"].format(sheet = sheet_name)
    st.components.v1.iframe(sheet, width = w, height = h)

def sidebar_setup():
    st.markdown("""
    <style>
    .between {
        height: 52vh;
    }
    .sidebar-footer {
        display: flex; 
        flex-direction: row; 
        justify-content: space-between;
        align-items: center;
        padding: 0 30%; 
    }
    [data-testid=stSidebarUserContent] {
        padding-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)
    with st.sidebar:
        st.page_link('Welcome.py', label='Welcome')
        st.page_link('pages/Stars_Rating_Analysis.py', label='1. Analysis of Stars Rating')
        st.page_link('pages/Notable_categories.py', label='2. Notable product categories')
        st.page_link('pages/Most_bought_categories_analysis.py', label='3. Analysis of most bought categories')
        st.page_link('pages/Unique_most_bought_category.py', label='4. A unique most bought categories')
        st.page_link('pages/Naming_of_top_products.py', label='5. Naming of top products')
        st.markdown('<div class="between"></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-footer">
            <a href="https://www.linkedin.com/in/anhphan1211" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/></svg>
            </a>
            <a href="https://www.github.com/justpqa" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            </a>
        </div>
        """, unsafe_allow_html=True)