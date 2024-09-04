import streamlit as st
from utils import *

def main():
    sidebar_setup()
        
    st.title("How ⭐ matter in Amazon UK Market")

    st.markdown(
        """
        One of the most important features of online market is how users can rate product based on their experience with Stars,
        and this is also an important features that buyers look into before decide on buying a product. Here, we will explore more how
        product at different "Star range" would look like in terms of prices, amount bought, etc.
        """
    )

    st.markdown(
        """
        #### Star Rating vs. Amount Bought
        We first can look into how stars rating related to what might be the most important metrics of a product, amount of products bought of an average product.
        """
    )
    
    show_tableau_graph("Sheet1", 600, 600)

    st.markdown(
        """
        As expected, the average amount of products bought in categories with higher average rating would be higher,
        but we can also see how spreaded the high-rating group is when compared to lower ratings, 
        especially when we look at how there are 3 categories with the average amount bought per product in categories is over 400,
        while majority of categories with at least 4 stars average rating has less than 200 products per product in average, 
        which means that there are still product categories with good products in general but really not as needed as other.
        """
    )

    st.markdown(
        """
        #### Star Rating vs. Average Price
        We also can look at the distribution of price across different star rating, 
        since some people would often prefer cheap product but are still good than more expensive product.
        """
    )
    
    show_tableau_graph("Sheet2", 600, 600)

    st.markdown(
        """
        Contrary to the previous graph, we can see here how categories with lower average star ratings often have a higher price,
        and the groups of lower ratings are often more varied in the average price of category. 
        When we look at the categories with higher star ratings, we can see how they are consistant in the categories' average price,
        and the price are lower than those of lower stars, which might indicate how low price would affect how people look at products of a certain type. 
        """
    )
    
    st.markdown(
        """
        #### Star Rating vs. Proportion of Best Selling products
        As Best Selling Tag is often considered to be an important facor that attracts users to certain products, 
        we can also try to look at the Best-Selling-ness of different categories at different ratings
        """
    )

    show_tableau_graph("Sheet3", 600, 600)
    
    st.markdown(
        """
        We can easily notice how categories with higher rating would lead to slightly higher proportion of products with Best Selling Tag.
        However, we also need to notice how the variance also increase greatly as well, with the only exception being the group of 3-4 stars. 
        This might also affected by the fact that the many high rating categories could have different popularity that contribute to their Best Selling status,
        versus the products with lower star ratings are often bad products that will definitely not become Best Selling. 
        However it's still surprise to see low stars categories with decent rate of products with Best Selling Tag like Material Handling Product (0.8 average Stars Rating, but 1 out of 40 products has Best Selling Tag).
        """
    )
    
if __name__ == "__main__":
    main()