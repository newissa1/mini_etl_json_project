"# Mini ETL JSON Project

This is a simple ETL (Extract, Transform, Load) dashboard built with **Streamlit** and **Docker**.

## 🚀 Features
- Reads JSON sales data
- Displays it in an interactive Streamlit dashboard
- Runs inside a Docker container

## 📦 To Run

```bash
docker build -t mini-etl-dashboard 
docker run -p 8501:8501 -v \"$(pwd)/data\":/app/data mini-etl-dashboard