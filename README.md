# Stock Data ETL Pipeline

## Overview

This project implements a simple **ETL (Extract, Transform, Load) data pipeline** that collects historical stock market data, processes it, and stores it in a PostgreSQL database for analysis.

The pipeline demonstrates core **data engineering concepts**, including automated data extraction, data transformation, and loading structured data into a relational database.

Stock data is retrieved from Yahoo Finance using the `yfinance` Python library.

---

## What This Project Does

The pipeline performs the following steps:

1. **Extract**

   * Downloads historical stock price data from Yahoo Finance.

2. **Transform**

   * Cleans the dataset.
   * Calculates additional metrics such as daily returns and moving averages.

3. **Load**

   * Stores the processed data in a PostgreSQL database table for querying and analysis.

---

## Technologies Used

* Python
* PostgreSQL
* Pandas
* SQLAlchemy
* yfinance

---

## Project Structure

```
stock-data-pipeline/
│
├── data/
│   ├── raw_stock.csv
│   └── processed_stock.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/stock-data-pipeline.git
cd stock-data-pipeline
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## Database Setup

Make sure PostgreSQL is installed and running.

### Step 1: Open PostgreSQL

From your terminal:

```
psql -U postgres
```

### Step 2: Create the Database

```
CREATE DATABASE stocks;
```

Connect to the new database:

```
\c stocks
```

---

## Creating the Table

Create the table that will store the processed stock data:

```
CREATE TABLE stock_prices (
    date TIMESTAMP,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT,
    daily_return FLOAT,
    ma_7 FLOAT,
    ma_30 FLOAT
);
```

You can verify the table was created:

```
\dt
```

---

## Running the Pipeline

Run the pipeline scripts in order:

### 1. Extract Stock Data

```
python src/extract.py
```

This downloads historical stock prices and saves them as:

```
data/raw_stock.csv
```

---

### 2. Transform the Data

```
python src/transform.py
```

This step:

* Cleans the dataset
* Calculates daily returns
* Calculates moving averages

The processed data is saved as:

```
data/processed_stock.csv
```

---

### 3. Load Data into PostgreSQL

```
python src/load.py
```

This step inserts the processed dataset into the `stock_prices` table.

---

## Verifying the Data

Connect to the database:

```
psql -U postgres -d stocks
```

Run a query:

```
SELECT * FROM stock_prices LIMIT 10;
```

To check the number of rows:

```
SELECT COUNT(*) FROM stock_prices;
```

---

## Example Data

The stored table contains the following fields:

| Column       | Description             |
| ------------ | ----------------------- |
| date         | Trading date            |
| open         | Opening price           |
| high         | Highest price           |
| low          | Lowest price            |
| close        | Closing price           |
| volume       | Trading volume          |
| daily_return | Daily percentage change |
| ma_7         | 7-day moving average    |
| ma_30        | 30-day moving average   |

---

## Skills Demonstrated

This project demonstrates:

* Building an ETL data pipeline
* Extracting financial data from APIs
* Data transformation with Pandas
* Loading structured data into PostgreSQL
* Writing SQL queries for data validation

---

## Future Improvements

Possible extensions include:

* Scheduling the pipeline with Apache Airflow
* Deploying the pipeline using Docker
* Adding automated data quality checks
* Creating a dashboard for stock analytics

---

## Author

Developed as a portfolio project demonstrating practical data engineering skills.
