# Databricks notebook source
snowflake_table = (spark.read
  .format("snowflake")
  .option("host", "btelligent.eu-central-1.snowflakecomputing.com")
  .option("port", "443") # Optional - will use default port 443 if not specified.
  .option("user", "meik_truschkowski")
  .option("password", "xxxxxxxxx")
  .option("sfWarehouse", "demo_wh")
  .option("database", "amazon_vendor_analytics__sample_dataset")
  .option("schema", "public") # Optional - will use default schema "public" if not specified.
  .option("dbtable", "product_catalog")
  .load()
)

# COMMAND ----------

snowflake_table.show(100)

# COMMAND ----------

display(snowflake_table)
