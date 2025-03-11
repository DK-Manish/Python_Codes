from azure.storage.blob import BlobServiceClient

# Replace these values with your actual Azure Storage connection strings
source_connection_string = ""
destination_connection_string = ""

# Replace these values with your actual container names
source_container_name = "<source_container_name>"
destination_container_name = "<destination_container_name>"

# Keyword to search for
keyword = "<file_keyword>"

# Connect to your Azure Storage account
source_blob_service_client = BlobServiceClient.from_connection_string(source_connection_string)
destination_blob_service_client = BlobServiceClient.from_connection_string(destination_connection_string)

# Get the source and destination container clients
source_container_client = source_blob_service_client.get_container_client(source_container_name)
destination_container_client = destination_blob_service_client.get_container_client(destination_container_name)

# List blobs in the source container
blob_list = source_container_client.list_blobs()

# Iterate through each blob in the source container
for blob in blob_list:
    blob_client = source_blob_service_client.get_blob_client(source_container_name, blob.name)

    # Check if the keyword is present in the file
    blob_data = blob_client.download_blob().readall().decode("utf-8")
    if keyword in blob_data:
        # If keyword is found, move the blob to the destination container
        destination_container_client.upload_blob(name=blob.name, data=blob_data)

        # Uncomment the line below to delete the source file after moving
        # blob_client.delete_blob()
