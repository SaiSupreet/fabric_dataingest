Fabric Pipeline & Spark ETL Solution Script
# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Initialize Spark Session
spark = SparkSession.builder.appName("Microsoft Fabric ETL").getOrCreate()

# Step 1: Read data from HTTP Source
source_url = "https://raw.githubusercontent.com/MicrosoftLearning/dp-data/main/sales.csv"
df = spark.read.format("csv").option("header", "true").load(source_url)

# Step 2: Add transformations - Add Year and Month columns
df = df.withColumn("Year", year(col("OrderDate"))).withColumn("Month", month(col("OrderDate")))

# Step 3: Add FirstName and LastName columns
df = df.withColumn("FirstName", split(col("CustomerName"), " ").getItem(0))
df = df.withColumn("LastName", split(col("CustomerName"), " ").getItem(1))

# Step 4: Filter and Reorder Columns
df = df.select("SalesOrderNumber", "SalesOrderLineNumber", "OrderDate", "Year", "Month", "FirstName", "LastName", "EmailAddress", "Item", "Quantity", "UnitPrice", "TaxAmount")

# Step 5: Save data as Delta table
df.write.format("delta").mode("append").saveAsTable("sales")

# Optional: Save transformed data to specific location (e.g., Parquet)
df.write.mode("overwrite").parquet("/path/to/save/transformed_data")

# Step 6: Clean up workspace (Manual step - instruct users to delete workspace in the UI)
print("Please remove the workspace manually via Microsoft Fabric settings if not needed.")

# End Spark Session
spark.stop()

Notes:

Ensure the .py script is run in an environment with Microsoft Fabric access.

Any images or missing options are described within the comments to guide the user where manual UI actions are needed, like creating workspaces or deleting resources.

This script automates the ETL workflow in Microsoft Fabric using PySpark and includes instructions on managing data ingestion, transformations, and loading.
