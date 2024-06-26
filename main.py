from google.cloud import bigquery

# Replace with your project ID
project_id = "fleet-geode-425017-g6"

# Define the BigQuery dataset and table names
dataset_id = "plsDontDelete"
table_id = "customer_data"

# Function to insert data into BigQuery table
def insert_data_to_bigquery(data):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Convert data to a list of rows (assuming data is a list of dictionaries)
    rows_to_insert = [dict(row) for row in data]

    table = client.get_table(table_ref)  # Get the table schema

    try:
        errors = client.insert_rows(table, rows_to_insert)
        if not errors:
            print("Data inserted successfully!")
        else:
            for err in errors:
                print(f"Error: {err}")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Example usage (replace with your actual data)
data = [
    {"name": "Tharun", "age": 30, "city": "New York", "credit_card_no": 458759248744, "cvv": 547},
    {"name": "Sunny", "age": 25, "city": "London", "credit_card_no": 874595474547, "cvv": 458},
    {"name": "Prem", "age": 18, "city": "Bengaluru", "credit_card_no": 785574564554, "cvv": 478}
]

insert_data_to_bigquery(data)
