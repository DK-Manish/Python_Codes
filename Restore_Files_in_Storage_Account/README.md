# Restore Deleted Blobs from an Azure Storage Container

## Overview
This script automates the restoration of **soft-deleted** blobs in an Azure Storage container. It connects to an **Azure Storage Account** using the `azure-storage-blob` Python SDK, retrieves the list of deleted blobs, and restores them using the **undelete_blob()** function.

The script ensures that any mistakenly deleted blobs can be recovered within the **soft delete retention period**.

## Prerequisites
Before running the script, ensure you have the following:
- An **Azure Storage Account** with **Soft Delete** enabled.
- A **Storage Container** where blobs were deleted.
- Python installed on your system.
- The `azure-storage-blob` package installed.

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
python restore_deleted_blobs.py
```

## Notes
- Ensure **Soft Delete** was enabled before the blobs were deleted. Otherwise, recovery is not possible.
- This script **restores all deleted blobs** in the container that are still within the retention period.
- If the **undelete option is missing in Azure Portal**, use this script to restore your blobs programmatically.

## License
This script is open-source and can be modified as needed.