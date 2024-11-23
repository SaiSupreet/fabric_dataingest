Microsoft Fabric Pipeline & Spark ETL Solution
This project showcases data ingestion, transformation, and management using Microsoft Fabric's lakehouse, pipelines, and Spark notebooks.

Prerequisites
Microsoft Fabric trial or equivalent
Familiarity with PySpark
Overview
Workspace Setup: Create a workspace in Microsoft Fabric.
Lakehouse Setup: Create a lakehouse with a new_data folder.
Pipeline Creation: Use Copy Data activity to ingest data.
Spark Notebook: Transform data with a notebook using PySpark.
Pipeline Integration: Link the pipeline and Spark notebook for ETL automation.
Data Verification: Validate data in the new_sales lakehouse table.
Steps
Workspace & Lakehouse Setup

Create a workspace and a lakehouse (new_data folder for ingestion).
Data Ingestion Pipeline

Copy sales data (sales.csv) from an HTTP source to new_data.
Notebook Transformation

Transform data and load it into a Delta Lake table (sales).
Pipeline Integration

Use a notebook activity to process and append to new_sales.
Clean Up

Delete the workspace when done.
Key Concepts
Lakehouse: Combines the best of data lakes and warehouses.
Pipelines: Automate data ingestion and processing.
Apache Spark: Perform scalable transformations.
Dependencies
Microsoft Fabric Trial
PySpark
Optional: Matplotlib & Seaborn for data visualization.
Future Enhancements
Automate pipeline runs.
Add data validation.
Integrate Power BI for visualization.
