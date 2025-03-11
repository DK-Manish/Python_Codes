import pandas as pd
from azure.cosmos import CosmosClient

# DB Credentials
cosmos_db_endpoint = ""  # give the cosmos end point
cosmos_db_key = "<cosmos_key_value>"
database_name = "<cosmos_database_name>"
container_name = "<cosmos_container_name>"

# Initialize Cosmos DB client
client = CosmosClient(cosmos_db_endpoint, cosmos_db_key)

# Get a reference to the database and container
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Define the query
query = """<query>"""

# Execute the query
result_iterable = container.query_items(query, enable_cross_partition_query=True)

# Convert query results to a list
results = [item['dataheader'] for item in result_iterable]

# Normalize the JSON into a DataFrame
df = pd.json_normalize(results)

# Specify the CSV file path
csv_file_path = "output.csv"

# Export the DataFrame to CSV
df.to_csv(csv_file_path, index=False)

print(f"Results exported to {csv_file_path}")