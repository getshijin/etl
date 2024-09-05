from sqlalchemy import create_engine
import pandas as pd
import sqlite3
import mysql.connector
from mysql.connector import Error

def extract_data():
    # Example: Extract data from a CSV file
    data = pd.read_csv('data/orders.csv')
    return data

# Transform
def transform_data(data):
    # Example: Simple transformation
    data['new_column'] = data['customer_id'] * 2
    return data

# Load
def load_data(data):
    # Example: Load data into a PostgreSQL database
    engine = create_engine('postgresql://postgres:root@localhost:5432/greencycle')
    data.to_sql('orders', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    data = extract_data()
    data = transform_data(data)
    load_data(data)
    print("finish")
