import csv
import os
from datetime import datetime
import time

import mysql.connector
from mysql.connector import Error

data_dir = "./data"

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',          # replace with your host, e.g., 'localhost'
            database='customer_data',        # replace with your database name
            user='root',      # replace with your database username
            password='mypassword'   # replace with your database password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def create_table():
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS events (
        event_time DATETIME,
        event_type VARCHAR(255),
        product_id BIGINT,
        category_id BIGINT,
        category_code VARCHAR(255),
        brand VARCHAR(255),
        price DECIMAL(10, 2),
        user_id BIGINT,
        user_session VARCHAR(255)
    );
    """

    try:
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print("Error while creating table:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



def parse_datetime(datetime_str):
    # Parses the datetime string and returns it in a MySQL-compatible format
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

def batch_import_csv(file_path, batch_size=200000):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    # Define your SQL INSERT query here
    insert_query = """
    INSERT INTO events (event_time, event_type, product_id, category_id, category_code, brand, price, user_id, user_session) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            batch = []

            for row in csv_reader:
                row[0] = parse_datetime(row[0])
                batch.append(tuple(row))
                if len(batch) == batch_size:
                    print(f"Importing {batch_size} entries.")
                    cursor.executemany(insert_query, batch)
                    connection.commit()
                    batch = []

            if batch:
                print(f"Importing {len(batch)} entries.")
                cursor.executemany(insert_query, batch)
                connection.commit()

    except Error as e:
        print("Error while importing data:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours > 0:
        return f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    elif minutes > 0:
        return f"{int(minutes)} minutes, {int(seconds)} seconds"
    else:
        return f"{int(seconds)} seconds"



create_table()

# Loop through all files in the directory
for file_name in os.listdir(data_dir):
    # Construct the full file path
    file_path = os.path.join(data_dir, file_name)

    # Check if the file is a CSV
    if file_path.endswith('.csv'):
        # Execute the function with the path to the CSV file
        print(f"Start Import: {file_path}")
        start_time = time.time()
        batch_import_csv(file_path)
        elapsed = time.time() - start_time
        print(f"Importing: {file_path} took {format_time(elapsed)}")



