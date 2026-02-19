# Enterprise Data Engineering Pipeline & Real-Time Alert System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![MSSQL](https://img.shields.io/badge/Microsoft%20SQL%20Server-Data%20Warehouse-red?style=flat&logo=microsoft-sql-server)
![Power BI](https://img.shields.io/badge/Power%20BI-Business%20Intelligence-F2C811?style=flat&logo=power-bi)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-2CA5E0?style=flat&logo=telegram)

## Project Description

This repository hosts a hybrid data engineering solution designed to simulate real-world data processing scenarios. The system integrates **Batch Processing** for corporate data, **Stream Processing** for financial market data, and an **Event-Driven Alert System** utilizing a centralized Microsoft SQL Server Data Warehouse.

The primary objective of this project is to demonstrate the implementation of robust, fault-tolerant ETL pipelines, automated workflows, and real-time monitoring without relying on enterprise-grade tools, showcasing raw coding proficiency in Python and SQL.

## System Architecture

The project consists of three main independent modules:

### 1. Batch ETL Module (`etl_pro.py`)
This module handles static data files (CSV/Excel) representing corporate employee records.
* **Extraction:** Reads raw data sources dynamically.
* **Transformation:** Applies data cleaning, type casting, and business logic validation.
* **Loading:** Uses SQLAlchemy and PyODBC for high-performance data insertion into MS SQL Server.
* **Error Handling:** Implements a comprehensive `try-except` mechanism to manage operational failures and logs incidents to a local file.

### 2. Real-Time Streaming & Alerting Module (`canli_veri.py`)
This module connects to external APIs to fetch live financial data and provides autonomous monitoring.
* **Data Source:** Binance Public API (BTC/USDT).
* **Ingestion:** Fetches JSON data at set intervals (simulating streaming).
* **Storage:** Appends real-time data to the SQL Server for historical analysis.
* **Event-Driven Alerts:** Integrates with the **Telegram Bot API** to send instant push notifications to mobile devices when critical price thresholds are breached.
* **Visualization:** Designed to feed a live Power BI Dashboard.

### 3. Automation (`run_pipeline.bat`)
* Contains Windows Batch scripts configured with **Task Scheduler** to execute the pipelines automatically at specific time intervals, ensuring data freshness.

## Technical Stack

* **Programming Language:** Python 3.x
* **Libraries:** Pandas, Requests, SQLAlchemy, PyODBC
* **Database:** Microsoft SQL Server (Express Edition)
* **Visualization:** Microsoft Power BI Desktop
* **Notifications:** Telegram Bot API
* **Version Control:** Git & GitHub

## Installation and Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/ensar-sencan/Python-MSSQL-Data-Engineering.git](https://github.com/ensar-sencan/Python-MSSQL-Data-Engineering.git)
    ```

2.  **Install Dependencies**
    ```bash
    pip install pandas sqlalchemy pyodbc requests
    ```

3.  **Database Configuration**
    Update the connection string in `etl_pro.py` and `canli_veri.py` to match your local SQL Server instance. Make sure to add your Telegram Bot Token in `canli_veri.py`.

## Author
**Ensar Sencan**
*Computer Engineering Student & Data Engineer*
