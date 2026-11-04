# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "ecd92ee1-74b5-4bfb-a940-cc4661126a50",
# META       "default_lakehouse_name": "LH_Bronze",
# META       "default_lakehouse_workspace_id": "8725e8db-1689-4f37-92e1-9470f87f1092",
# META       "known_lakehouses": [
# META         {
# META           "id": "ecd92ee1-74b5-4bfb-a940-cc4661126a50"
# META         },
# META         {
# META           "id": "e1948a4e-f617-41fd-9a8e-a7496a7507b7"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

csv_path = "abfss://dev_WS@onelake.dfs.fabric.microsoft.com/LH_Bronze.Lakehouse/Files/raw_sales"

df = spark.read.option("header", "true")\
                .option("inferSchema", "true")\
                .csv(csv_path)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_unitPrice = df.withColumn("unitPrice", df["Total"] / df["Quantity"])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_unitPrice)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

silver_lh_path = "abfss://dev_WS@onelake.dfs.fabric.microsoft.com/LH_silver.Lakehouse/Tables/sales"

df.write.format("delta")\
        .mode("overwrite")\
        .option("overwriteSchema", "true")\
        .save(silver_lh_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
