from azure.storage.blob import BlobServiceClient

# Connection string and container name
connection_string = "<connection_strring>"
container_name = "<container_name>"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Restore deleted blobs
for blob in container_client.list_blobs(include=["deleted"]):
    print(f"Restoring: {blob.name}")
    container_client.get_blob_client(blob.name).undelete_blob()
    print(f"Restored: {blob.name}")

print("All deleted blobs have been restored successfully!")
