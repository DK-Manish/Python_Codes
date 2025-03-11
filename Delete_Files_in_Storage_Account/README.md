# Delete CSV Files from an Azure Storage Container

## Overview
This script automates the deletion of `.csv` files from a specified **Azure Storage container**. It connects to an **Azure Storage Account** using the `azure-storage-blob` Python SDK, retrieves the list of blobs in the container, and deletes only those files that have a `.csv` extension.

The script ensures efficient management of blob storage by removing unnecessary CSV files while preserving other data types. It can be executed manually or scheduled as part of an automated workflow.

## Prerequisites
Before running the script, ensure you have the following:
- An **Azure Storage Account**
- A **Storage Container** with blobs
- Python installed on your system
- The `azure-storage-blob` package installed

## Installation
Install the required Azure SDK package using pip:
```sh
pip install azure-storage-blob
```

## Configuration
Update the script with your Azure Storage connection details:
1. Replace `<connection_string>` with your **Azure Storage Account connection string**.
2. Replace `<container_name>` with your **Azure Storage container name**.

## Execution
Run the script using Python:
```sh
python delete_csv_files.py
```

## Notes
- Ensure **Soft Delete** is enabled in your storage account if you want the ability to recover deleted files.
- Running this script **permanently deletes all CSV files** in the specified container.
- Modify the script to filter other file types if needed.

## License
This script is open-source and can be modified as needed.