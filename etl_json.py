import json 
import os
import sqlite3 
import pandas as pd


# to extract data
def extract_data(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)    
    return pd.DataFrame(data)

# to transform data
def transform_data(df):
    df['total'] = df['quantity'] * df['price']
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

# to load data
def load_to_sqlite(df,db_path,table_name='sales'):
    conn=sqlite3.connect(db_path)
    df.to_sql(table_name, conn , if_exists ='replace', index=False )
    conn.close()

# to run the ETL

if __name__ == "__main__":
    json_path='data/sales.json'
    db_path =  'database.db'

if not os.path.exists(json_path):
    print("Json file not found")
else:
    df= extract_data(json_path)
    df_transformed = transform_data(df)
    load_to_sqlite (df_transformed, db_path)
    print("ETL pipeline from JSON completed successfully.")     