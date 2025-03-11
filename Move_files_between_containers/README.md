# Move Blobs Between Azure Storage Containers Based on a Keyword

## Overview
This script automates the process of moving blobs from one Azure Storage container to another based on a specified keyword in the file content. It connects to an **Azure Storage Account**, retrieves the list of blobs, checks if the keyword exists within the file, and moves matching files to a destination container.

## Prerequisites
Before running the script, ensure you have the following:
- An **Azure Storage Account**.
- A **Source and Destination Storage Container**.
- Python installed on your system.
- The `azure-storage-blob` package installed.

## Installation
Install the required Azure SDK package using pip:
```sh
pip install azure-storage-blob
```

## Configuration
Update the script with your Azure Storage details:
1. Replace `<source_connection_string>` and `<destination_connection_string>` with your **Azure Storage connection strings**.
2. Replace `<source_container_name>` and `<destination_container_name>` with your **actual container names**.
3. Replace `<file_keyword>` with the keyword that needs to be searched in the file content.

## Execution
Run the script using Python:
```sh
python move_blobs.py
```

## Notes
- The script checks for the keyword **inside the file content**, not the file name.
- If a match is found, the file is copied to the destination container.
- To **delete the original file from the source container** after moving, **uncomment** the `blob_client.delete_blob()` line in the script.
- Ensure that **Soft Delete** is enabled in your storage account if you want the ability to recover deleted files.

## License
This script is open-source and can be modified as needed.

## Author
[Your Name]
