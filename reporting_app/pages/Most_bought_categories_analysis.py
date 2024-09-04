import streamlit as st
from utils import *

def main():
    st.set_page_config(page_title='Amazon UK Analysis')
    
    sidebar_setup()
    
    st.title("Analysis of some categories that were most bought in Sep 2023")
    
    st.markdown(
        """
        As we look at notable categories of products in Amazon UK market, 
        we also dive deeper into categories that are often have more people buying, 
        in order to understand better how products inside rather popular categories different from each other.
        We will look at the two most bought in Sep 2023 categories in Amazon UK as noted in previous pages, 
        due to how similar are these two categories in rating and price. 
        Throughout this, we will see the similarity in the distribution of products metrics 
        as well as how better products of these categories separate themselves from other
        """
    )
    
    st.markdown(
        """
        #### Health & Personal Care ⚕️
        """
    )
    
    st.markdown(
        """
        We first look into the distribution of amount of each product that people bought in September 2023.
        """
    )
    
    show_tableau_graph("Sheet9", 600, 600)
    
    st.markdown(
        """
        We can notice how only a small amount of products were bought more than 1000 times each in Sep. 2023,
        and as the amount bought increase, the number of products that has that much bought decrease quickly.
        Based on this, we decided to consider two different groups, those with more than 1000 products (moreBought = True, contribute 13%),
        and 1000 or less. We will look into the price and stars distribution of these two groups:
        """
    )
    
    show_tableau_graph("Sheet10", 600, 800)
    
    st.markdown(
        """
        One thing that we can notice is how the products that are bought more often have slightly lower prices than other, 
        which might allow people to prefer one product more than the other. 
        We can test this hypothesis to see if in average product with more people bought has lower prices:
        """
    )
    
    st.image("./images/hpc_price_ttest_2.png")
    
    st.markdown(
        """
        Based on the result of the test and the confidence interval of the difference between 2 groups, 
        we can see that the products with 1000 or more times bought are only about 2-3 dollars lower.
        Another factor that also make one product to be separate with other is how its wording in the title is different from other.
        And the next word clouds will show how most often words only in more selling product versus less selling product.
        """
    )
    
    show_tableau_graph("Dashboard1", 600, 800)
    
    st.markdown(
        """
        It seems that while there is no important words that are only inside products that are more sought after, 
        there are some notables words that are most seen among titles of less bought products like: vape, vibrator, accessories, etc.,
        which might indicate some type of products that does not attract users or often not have good reviews. 
        This can be a notable signal for online market to note when choosing certain products to sell on their platform.
        """
    )
    
    st.markdown(
        """
        #### Grocery Products 🍎
        """
    )
    
    st.markdown(
        """
        Since Grocery category is also a popular category with high amount bought per product, 
        as well as slightly higher star ratings and lower price comparing to Health & Personal Care, 
        we can also look into this category to see how does these popular low prices categories look like. 
        We first will also look into how does the distribution of amount bought for each product look like
        """
    )
    
    show_tableau_graph("Sheet13", 600, 600)
    
    st.markdown(
        """
        Here, we can see an even more skewed distribution, 
        with the majority of products were bought less than 500 times in Sep 2023,
        and we found that only 7 percents of products has more than 1000 bought, 
        so this seems like it is even harder to climb to the top in this product category (based on how heavily skewed the distribution).
        This makes it even more curious to look at if this minority group of sought after product looks like.
        (Here, we denote a product as it has more people to buy it in Sep 2023 the same way as we defined in Health & Personal Care category)
        """
    )
    
    show_tableau_graph("Sheet14", 600, 800)
    
    st.markdown(
        """
        We can see the same story in this category comparing to the Health & Personal Care category,
        and the difference between the price of the two groups seems to be even smaller in this category.
        Using the same test as we did for previous category, we can look closer into how lower is the more bought products comparing to the rest:
        """
    )
    
    st.image("./images/g_price_ttest_2.png")
    
    st.markdown(
        """
        We notice how the difference between price of the two categories is smaller, only from 1-2.5 dollars lower, 
        while the average price of this category is almost the same as the previous category, 
        which might indicate how this could also be a factor for a product of this category to be more bought. 
        In addition to this, as naming of a product is also important, 
        we can also look into the most occured words that are unique to title of each group, 
        which could be used as a guide for naming products of this category.
        """
    )
    
    show_tableau_graph("Dashboard2", 600, 800)
    
    st.markdown(
        """
        #### What next?
        While some of the most bought categories in this section (as well as in the graph in previous page), 
        notice that there are one group that has higher price and significantly lower rating among other, 
        that is Professional Medical Supplies product. In the next page, an even greater difference will be unveiled,
        that show how is it hard to become more sought after and what does the previous factors (price, title) would affect this. 
        """
    )
    
if __name__ == "__main__":
    main()