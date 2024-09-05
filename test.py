import psycopg2
from psycopg2 import OperationalError
import pandas as pd

def verify_postgresql_password(host, port, dbname, user, password):
    try:
        # Try to connect to the database
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        # If the connection is successful, return True
        connection.close()  # Close the connection
        return True
    except OperationalError as e:
        # If the connection fails, return False
        return False

# Example usage
host = "localhost"
port = 5432
dbname = "demo"
user = "postgres"
password = "password"

a= pd.read_csv('data/orders.csv')
print(a)

if verify_postgresql_password(host, port, dbname, user, password):
    print("Password is correct.")
else:
    print("Password is incorrect.")
