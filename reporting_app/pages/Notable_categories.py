import streamlit as st 
from utils import *

def main():
    st.set_page_config(page_title='Amazon UK Analysis')
    
    sidebar_setup()
        
    st.title("Some Notable Categories on Amazon UK")

    st.markdown(
        """
        #### Most Bought Category on Amazon UK 🛒
        When we analyze different products on Amazon, one metrics that vendors care the most is the amount of product bought, so here we looked into the most bought categories (w.r.t the number of products.
        Specifically, we will look quickly into the top 20 most bought categories (calculated by the average amount of product bought per product)
        """
    )
    
    show_tableau_graph("Sheet5", 800, 600)

    st.markdown(
        """
        One main thing that we can notice here is most of the top categories have rather lower average prices, 
        except for Professional Medial Supplies, which has a pretty high average price in the category (about $300), 
        and it also have pretty low average ratings comparing to other categories (2.0 average rating comparing to about 4.0 rating in other most bought category).
        Contrary to this, Health & Personal Care or Grocery has a rather low price but also most sought after (in Sep 2023) and has a pretty high average rating (4.4).
        These might indicate which categories that vendor would focus into when they join a giant online market like Amazon. 
        """
    )

    st.markdown(
        """
        ** We will dive into how these notable categories look like <a href="http://localhost:8501/Most_bought_categories_analysis" target="_self">here</a> **
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        #### Categories with most "Best Selling" product 🏷️
        Another thing that also caught my interest is how there are some categories that will attract more people to buy rather than some other,
        some type of products would be more popular on Amazon, so I also dive into the categories with rather high proportion of best selling products
        """
    )
    
    show_tableau_graph("Sheet6", 800, 600)

    st.markdown(
        """
        It comes to my surprise that there are some categories that even though it has a pretty high rate of Best Selling Tag, 
        it still has higher price comparing to other, and it also a pretty high standard deviation of prices across products, 
        which show how varied are those categories. 
        Things like Billard & Pool or Professional Medical Supplies for example can have a variety of products, 
        and the prices are varied (for Pools, cues can be a few hundred dollars while chalk can be 5-10 dollars.) 
        It also comes to my surprise how some rather odd categories like Wind Instrument can have a rather high rate of Best Selling Tag, 
        it would be interesting to look at these categories in the Amazon market of other regions to see if it has same trend.
        At the same time, it might not be surprise to see how categories like these has lower rating in average, and similar to what we found in previous graph, 
        we might suspect a categories overall rating would be related to its average price or price spread.
        """
    )

if __name__ == "__main__":
    main()