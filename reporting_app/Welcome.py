import streamlit as st
from utils import *

def main():
    sidebar_setup()
        
    st.title("Analysis of UK Amazon Market in October 2023")
    
    st.subheader("Exploring Market Insights and Product Differentiation")

    st.markdown(
        """
        Welcome to the Amazon UK Product Analysis Dashboard! This application provides a comprehensive analysis 
        of a dataset containing about 2 million products from Amazon UK in October 2023. Whether you're a business strategist, 
        a data enthusiast, or just curious about market trends, this tool offers valuable insights into the 
        competitive landscape of products available on Amazon UK.
        
        ### Key Features:
        - ⭐ **Star Ratings Analysis**: Dive deep into the distribution of star ratings across various products, 
        and uncover how customer feedback shapes the perception of products in the market.
        - 📊 **Category Insights**: Identify the most bought categories and discover which categories host the 
        best-selling products on Amazon UK.
        - 🔍 **In-Depth Category Analysis**: Explore detailed insights on some of the most popular product categories, 
        examining factors that contribute to their high sales.
        - 🛒 **Peculiar Category Analysis**: Investigate a more sought-after category that stands out due to unusual 
        characteristics, such as star ratings or pricing trends.
        - 🏷️ **Product Naming Trends**: Take a closer look at how top-selling products are named, revealing patterns 
        in naming conventions that might influence buyer behavior.

        ### How to Use:
        Navigate through the sidebar to access different sections of the analysis. Each section offers 
        interactive visualizations and detailed breakdowns to help you uncover meaningful insights.
        """
    )
    
    st.info("Get started by selecting a section from the sidebar!")
    
if __name__ == "__main__":
    main()