import boto3
import pymysql
import pandas as pd
import os
S3_BUCKET = "your-s3-bucket-name"
FILE_NAME = "data.csv"
GLUE_DATABASE = "glue_database"
GLUE_TABLE = "glue_table"

RDS_HOST = "your-rds-endpoint"
RDS_USER = "admin"
RDS_PASSWORD = "your-password"
RDS_DB = "your-database"

s3 = boto3.client("s3")

try:
    # Download file from S3
    s3.download_file(S3_BUCKET, FILE_NAME, FILE_NAME)
    df = pd.read_csv(FILE_NAME)

    # Connecting to RDS for further config to happen
    connection = pymysql.connect(
        host=RDS_HOST,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB
    )
    
    cursor = connection.cursor()
    
    for _, row in df.iterrows():
        cursor.execute(f"INSERT INTO your_table (col1, col2) VALUES ('{row['col1']}', '{row['col2']}')")

    connection.commit()
    print("✅ Data inserted into RDS successfully")

except Exception as e:
    print(f"⚠️ Error inserting into RDS: {e}")
    
    # if RDS fails bychance then pushing the date to AWS glue
    glue = boto3.client("glue")
    glue.create_table(
        DatabaseName=GLUE_DATABASE,
        TableInput={
            "Name": GLUE_TABLE,
            "StorageDescriptor": {
                "Columns": [
                    {"Name": "col1", "Type": "string"},
                    {"Name": "col2", "Type": "string"}
                ]
            }
        }
    )
    print("✅ Data pushed to Glue successfully")
