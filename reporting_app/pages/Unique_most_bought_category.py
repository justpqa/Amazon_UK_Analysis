import streamlit as st
from utils import *

def main():
    sidebar_setup()
    
    st.title("Analysis of some categories that were most bought in Sep 2023")
    
    st.markdown(
        """
        As similar to the previous 2 categories, we look into how the distribution of number of bought for products in this category looks like
        """
    )
    
    show_tableau_graph("Sheet17", 600, 600)
    
    st.markdown(
        """
        We notice that this time is it very hard to have someone to buy your products, 
        with majority of products does not have anyone bought last month 
        (only 11 percents of product were bought at least 1 times, 
        which show that is it as hard to have someone buy your product in this category as to have a lot of bought for your product in other categories).
        Based on this, it is important to analyze the difference between the 2 groups of no one bought and the rest, 
        looking at factors like naming, stars, price to separate these 2 groups.
        We first will look into the difference in star ratings and price of the 2 groups
        """
    )
    
    show_tableau_graph("Sheet18", 600, 800)
    
    st.markdown(
        """
        Notice how the product that has at least 1 person to buy in Sep 2023 has significantly lower price comparing to the other,
        (just about 30 dollars, versus 0 to 4000 dollars range in the other group). At the same time, the group of products with at least 
        1 person bought is less varied in terms of stars rating and often pretty high, comparing to the lower stars rating and higher range of the other group.
        This show how well a certain groups perform comparing to other both in terms of rating and amount bought. 
        One thing that we might want to test is was there actually any difference in the prices between the two sides, 
        as well as how big is the difference in the ratings between having someone to buy your product or not,
        we can conduct Welch's t-test to check that: 
        """
    )
    
    st.image("./images/pms_price_ttest_2.png")
    
    st.image("./images/pms_star_ttest_2.png")
    
    st.markdown(
        """
        We can see how larger the difference between the 2 groups in this category comparing to the previous most bought categories that we found.
        This might be explained by how lower prices is not actually make a product to be more competitive than other, 
        it might be related to how there are some type of products will be bought more comparing to other types, 
        and the types of Professional Medical Supplies product that people often buy has significantly lower prices (based on the nature of the product itself),
        which leads to the problem of choosing the right products to sell in a certain market of some type of products.
        In addition to this, the difference in star ratings between the 2 groups is also sigficant (a 2.5 stars difference in rating can take a very very bad product to a good product),
        which motivates us even more to look into the difference between products of this cateogory. 
        Because of this, it is also important to also look into the words that are most occurs in titles of each of the groups (appear exclusively in 1 group),
        in order to see if we can decipher what type of products would be more easily to lead to profitability:
        """
    )
    
    show_tableau_graph("Dashboard3", 600, 800)
    
    st.markdown(
        """
        It seems like the groups of non-bought product were more spreaded and related to professional tools that nurses and doctors needed to perform,
        which can also explain why their prices are often higher than other, we can also see some words like "model" or "anatomy" or "education",
        which indicates how education products for possibly medical-related or nursing-related class were often more expensive and not really needed that often.
        At the same time, if we look at the words that only appears in products that has someone bought, we can see how some words might indicate the type of products:
        like "removal" is related to some ear wax removal kit that is needed by many people and needed more often, 
        or "suturing" related to suturing kit, which might be needed more often due to the need for emergency surgery in case of accident.
        From here, we can see the importance of identifying the needed products in a certain group in order to help your online shop to be sought after by more people,
        and a deeper analysis on the naming of product would allow us to gain more insight on more needed product in Amazon UK market.
        """
    )
    
    st.image("./images/pms_removal_product.png", caption = 'Some products that has "removal" in their title')
    
    st.image("./images/pms_suturing_product.png", caption = 'Some products that has "suturing" in their title')

    
if __name__ == "__main__":
    main()