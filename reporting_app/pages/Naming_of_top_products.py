import streamlit as st
from utils import *

def main():
    sidebar_setup()
        
    st.title("What are the names of some of the 'best' products on Amazon UK")

    st.markdown(
        """
        #### Top words inside most bought products
        """
    )

    show_tableau_graph("Sheet7", 600, 600)

    st.markdown(
        """
        #### Top words inside 5 stars product
        """
    )

    show_tableau_graph("Sheet8", 600, 600)
    
if __name__ == "__main__":
    main()