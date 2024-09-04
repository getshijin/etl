from sqlalchemy import create_engine
import pandas as pd


def extract_data():
    # Example: Extract data from a CSV file
    data = pd.read_csv('data/orders.csv')
    return data

# Transform
def transform_data(data):
    # Example: Simple transformation
    data['new_column'] = data['existing_column'] * 2
    return data

# Load
def load_data(data):
    # Example: Load data into a PostgreSQL database
    engine = create_engine('postgresql://username:password@localhost:5432/demo')
    data.to_sql('order', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    data = extract_data()
    data = transform_data(data)
    load_data(data)
