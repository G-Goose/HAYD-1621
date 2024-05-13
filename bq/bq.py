from google.cloud import bigquery

def create_bigquery_dataset_table():
    client = bigquery.Client()

    # Define your dataset
    dataset_id = f"{client.project}.hayd1621"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "EU"
    client.create_dataset(dataset, exists_ok=True)

    # Define your table
    table_id = "{}.mood_board".format(dataset_id)
    schema = [
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("value", "FLOAT"),
    ]
    table = bigquery.Table(table_id, schema=schema)
    client.create_table(table, exists_ok=True)

create_bigquery_dataset_table()
