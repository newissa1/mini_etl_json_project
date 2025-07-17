import json
import streamlit as st
import os 
import pandas as pd

# Load your JSON file
data_path = "data/sales.json"

if os.path.exists(data_path):  # <-- Fixed condition
    with open(data_path) as f:
        data = json.load(f)

    df = pd.DataFrame(data)  # <-- Also fixed: you used `sales` instead of `data`
    st.title("Mini ETL Dashboard") 
    st.write("Sales Data")      
    st.dataframe(df)
else:
    st.warning("No data found. Make sure sales.json is in the data/ directory.")
