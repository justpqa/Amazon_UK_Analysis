import streamlit as st
from utils import *

def main():
    st.set_page_config(page_title='Amazon UK Analysis')
    
    sidebar_setup()
        
    st.title("What are the names of some of the **best** products on Amazon UK")
    
    st.markdown(
        """
        I create these chart in the hope that this would give a quick view into how the naming of products would be different across best and worst products overall
        """
    )

    st.markdown(
        """
        #### Top words inside most bought products vs. least bought products
        """
    )

    show_tableau_graph("Dashboard4", 600, 800)

    st.markdown(
        """
        #### Top words inside 5 stars product vs. 0 stars product
        """
    )

    st.markdown(
        """
        (Notice how some products with name includes weird words (code, id?) appears inside this, 
        as well as there are some words like optique appear in the worst wordcloud of both dashboard
        """
    )
    show_tableau_graph("Dashboard5", 600, 800)
    
if __name__ == "__main__":
    main()