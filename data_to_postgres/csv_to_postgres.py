# import packages 
import psycopg2 
import pandas as pd 
from sqlalchemy import create_engine 
import os
from dotenv import load_dotenv
load_dotenv("../.env.postgres")
  
# establish connections 
conn_string = os.environ.get("POSTGRES_CONN")
db = create_engine(conn_string) 
conn = db.connect() 
print("Connected to db")
  
# import the csv file to create a dataframe 
data = pd.read_csv("./train.csv") 
print(data.head())
  
# converting data to sql 
data.to_sql('amazon_uk_2023', conn, if_exists= 'replace') 
print("Uploaded to Postgres")