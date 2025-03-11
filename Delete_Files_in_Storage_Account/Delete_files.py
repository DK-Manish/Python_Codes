#Deleting all the files from a container in Azure Storage Account

from azure.storage.blob import BlobServiceClient

connection_string = "<connection_string>"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Container name 
container_name = "<container_name>"

#List of blobs
container_client = blob_service_client.get_container_client(container_name)
blob_list = container_client.list_blobs()

# Delete JSON files
for blob in blob_list:
    if blob.name.endswith('.csv'):
        blob_client = container_client.get_blob_client(blob)
        blob_client.delete_blob()
        print(f"Deleted blob: {blob.name}")
