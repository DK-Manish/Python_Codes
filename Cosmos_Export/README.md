# Cosmos DB Query Script

This script connects to an **Azure Cosmos DB** container, executes a query to retrieve specific records, and exports the results to a CSV file.

## **Prerequisites**

Ensure you have the following installed before running the script:

- **Python 3.6+**
- **Required Python packages:**
  ```bash
  pip install azure-cosmos pandas
  ```
- **Access to an Azure Cosmos DB instance** with the correct endpoint and access key.

## **Script Overview**

### **1. Connecting to Cosmos DB**
- The script initializes a **CosmosClient** using the **Cosmos DB endpoint** and **access key**.
- It connects to the **database**  and the **container**

### **2. Executing the Query**

### **3. Processing the Results**
- The retrieved JSON data is **normalized into a Pandas DataFrame**.
- The DataFrame is then **exported to a CSV file (`output.csv`)**.

## **Usage**

1. Update the script with your **Cosmos DB credentials**:
   - `cosmos_db_endpoint`
   - `cosmos_db_key`

2. Run the script:
   ```bash
   python script.py
   ```

3. The results will be saved in `output.csv` in the same directory.

## **File Structure**
```
project-folder/
│── script.py  # Python script
│── output.csv  # Generated CSV file
```

## **Troubleshooting**
- Ensure the **Cosmos DB endpoint and key** are correct.
- If there are **no results**, verify that your query conditions match existing records.
- If encountering **Cosmos DB connection issues**, check firewall rules and access permissions.

## **Modifications**
- You can modify the query conditions based on different `dataheader` values.
- Change the **CSV file name** by updating `csv_file_path` in the script.

---
This script automates Cosmos DB querying and data extraction, making it easier to analyze and export structured data. 🚀
