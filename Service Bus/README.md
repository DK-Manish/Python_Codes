# Service Bus Integration

This folder contains the `Dead.py` script, which is designed for handling Azure Service Bus messages.

## Installation & Setup

Ensure you have Python installed, along with the necessary dependencies.

### Install Required Packages
Run the following command to install the necessary dependencies:
```bash
pip install azure-servicebus
```

## Usage

### 1. Update Configuration
Before running the script, update the **connection string** and **queue/topic details** in the `Dead.py` file.

### 2. Run the Script
Execute the script using:
```bash
python Dead.py
```

## Features
- Connects to an Azure Service Bus queue.
- Reads and processes messages from the queue.
- Handles message acknowledgment and error handling.

## Folder Structure
```
Python-Codes/
│── Service Bus/
│   ├── Dead.py  # Main script for handling Service Bus messages
│   ├── README.md  # Documentation for the Service Bus script
```

## Notes
- Ensure your Azure Service Bus namespace and queue/topic are correctly configured.
- Modify the script as needed to handle different message formats or logging mechanisms.

## Troubleshooting
If you encounter issues, verify:
- The connection string is correct.
- The queue/topic exists in the Azure portal.
- Required Python packages are installed.

For further debugging, use:
```python
print("Debug logs enabled")
```