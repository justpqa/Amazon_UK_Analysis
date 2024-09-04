# Amazon UK Analysis

## Project Overview

This project focuses on analyzing a dataset of approximately 2 million products from Amazon UK, collected in October 2023. Inspired by [this Kaggle dataset](https://www.kaggle.com/datasets/asaniczka/amazon-uk-products-dataset-2023), the goal is to leverage data visualization and basic statistical tools to gain meaningful insights into the Amazon UK market.

## Data Source

The data was sourced from Kaggle and represents a snapshot of Amazon UK's product listings as of October 2023. It includes a wide variety of products, categorized across multiple domains.

## Workflow

1. **Data Ingestion**:
    - The raw dataset was ingested into a PostgreSQL database for structured analysis.
    - Views and tables were created to facilitate easier querying and data exploration.

2. **Data Analysis**:
    - Python was used to perform detailed analysis on specific categories.
    - Seaborn was utilized extensively for creating informative and visually appealing statistical plots, helping to uncover trends and patterns within the data.
    - Identified the wording of top products to understand common patterns and trends.

3. **Visualization**:
    - Tableau was the primary tool for creating all visualizations, allowing for interactive exploration of the data and enabling deeper insights.
    - Seaborn and Matplotlib were also used for generating additional plots and visualizations to support the analysis.

4. **Results Presentation**:
    - Streamlit was utilized to display the analysis results in an interactive and user-friendly format, making it easy to navigate through the findings.

## Project Goals

The primary objective of this project is to employ data visualization, complemented by interpretable statistical tools, to analyze the Amazon UK market. The project aims to uncover notable insights, such as category-specific trends, product popularity, and effective product naming conventions.

### Key Insights:
- **Category Analysis**: Identified top-performing categories and their key characteristics.
- **Product Naming**: Analyzed the wording of top products to determine effective naming strategies.
- **Market Trends**: Visualized market trends and patterns across different categories using Tableau's interactive dashboards.

## Tools & Technologies

- **PostgreSQL**: For data storage and management.
- **Python**: For data processing, category analysis, and product wording identification.
- **Seaborn**: For creating detailed statistical visualizations to support analysis.
- **Tableau**: For creating interactive and comprehensive visualizations that provide deeper insights into the data.
- **Streamlit**: For building an interactive web app to present the analysis results.

## How to Run

1. **Database Setup**:
    - Ensure you have PostgreSQL installed and set up.
    - Ingest the dataset into your PostgreSQL database using the provided SQL scripts.

2. **Python Analysis**:
    - Run the Python scripts to perform the category-specific analysis, generate Seaborn visualizations, and extract insights on product wording.

3. **Tableau Visualization**:
    - Open the Tableau workbook to explore the visualizations and interact with the data.

4. **Streamlit App**:
    - Run the Streamlit app to interactively view and explore the results.

## Conclusion

This project provides a comprehensive analysis of the Amazon UK market, highlighting key trends and insights using a combination of data visualization and statistical analysis. By focusing on category-specific trends and product naming conventions, the project offers a detailed view of how the Amazon UK marketplace functions.

Through the use of Tableau and Seaborn, the project demonstrates the power of data visualization in uncovering meaningful insights from complex datasets.
