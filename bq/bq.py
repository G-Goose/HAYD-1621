import os
import pytz
from google.cloud import bigquery
from datetime import datetime


project_name = os.getenv('GCP_PROJECT')
dataset_name = os.getenv('BQ_DS')
table_name= os.getenv('BQ_TABLE')
location_name= os.getenv('BQ_LOCATION')

client = bigquery.Client()

def create_bigquery_dataset_table():
    # Define your dataset
    dataset_id = f"{client.project}.{dataset_name}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location_name
    client.create_dataset(dataset, exists_ok=True)

    # Define your table
    table_id = f"{dataset_id}.{table_name}"
    schema = [
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("value", "FLOAT"),
    ]
    table = bigquery.Table(table_id, schema=schema)
    client.create_table(table, exists_ok=True)

    return "Table created!"

def update_or_insert_value(new_value, project_id=project_name, dataset_id=dataset_name, table_id=table_name):
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    # Get today's date in the right timezone, usually UTC for BigQuery
    today = datetime.now(pytz.utc).date().strftime('%Y-%m-%d')
    print(today)
    print(type(today))

    # Construct the SQL to check for an existing row with today's date
    query = f"""
    SELECT value
    FROM `{project_id}.{dataset_id}.{table_id}`
    WHERE DATE(date) = '{today}'
    """
    query_job = client.query(query)
    results = list(query_job)

    # Check if there's an existing row for today
    if results:
        # Update the existing row
        update_query = f"""
        UPDATE `{project_id}.{dataset_id}.{table_id}`
        SET value = {new_value}
        WHERE DATE(date) = '{today}'
        """
    else:
        # Insert a new row
        update_query = f"""
        INSERT `{project_id}.{dataset_id}.{table_id}` (date, value)
        VALUES ('{today}', {new_value})
        """

    # Execute the update or insert query
    update_job = client.query(update_query)
    update_job.result()  # Wait for the job to complete

    return "Update successful" if results else "Insert successful"

def fetch_bigquery_table_as_dict( project_id=project_name, dataset_id=dataset_name, table_id=table_name):
    # Set up BigQuery client

    # Construct query using environment variables
    query = f"""
        SELECT `date`, `value`
        FROM `{project_id}.{dataset_id}.{table_id}`
    """

    # Execute the query and collect the results
    query_job = client.query(query)
    results = query_job.result()

    # Convert the results to a dictionary with date as key and value as value
    data_dict = {row['date']: row['value'] for row in results}

    return data_dict

# print(create_bigquery_dataset_table())
# print(update_or_insert_value(6))
# print(fetch_bigquery_table_as_dict())
