import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',  # replace with your host, e.g., 'localhost'
    database='customer_data',  # replace with your database name
    user='root',  # replace with your database username
    password='mypassword'  # replace with your database password
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a Faker instance to generate fake data
fake = Faker()
# Get the current date
current_date = datetime.now().date()
yesterday_date = current_date - timedelta(days=1)


# Generate and insert 10,000 entries into the table
def generate_mock_data(cur_date, amount):
    for _ in range(amount):
        event_time = datetime.combine(cur_date, datetime.min.time()) + timedelta(minutes=random.randint(0, 1439))
        event_time_formatted = event_time.strftime("%Y-%m-%d %H:%M:%S")
        event_type = random.choice(["view", "click", "purchase"])
        product_id = fake.random_int(min=1000000, max=9999999)
        category_id = fake.random_int(min=1000000000000000000, max=2053013555631882655)
        category_code = fake.random_element(
            elements=["electronics.smartphone", "appliances.sewing_machine", "computers.notebook"])
        brand = fake.company()
        price = fake.pyfloat(left_digits=3, right_digits=2, positive=True)
        user_id = fake.random_int(min=100000000, max=999999999)
        user_session = fake.uuid4()

        # SQL query to insert data into the table
        insert_query = """
        INSERT INTO events_live 
        (event_time, event_type, product_id, category_id, category_code, brand, price, user_id, user_session)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the query
        cursor.execute(insert_query, (
        event_time_formatted, event_type, product_id, category_id, category_code, brand, price, user_id, user_session))

    # Commit changes and close the database connection


# generate_mock_data(current_date, 100000)
generate_mock_data(yesterday_date, 100000)

conn.commit()
conn.close()

print("Data inserted successfully.")
