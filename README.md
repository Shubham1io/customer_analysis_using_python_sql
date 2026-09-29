# Customer Shopping Behavior Analysis — Python & SQL

An end-to-end **ETL pipeline** built with Python, Pandas, and MySQL to clean, transform, and analyze customer shopping data.

The project is structured as a modular ETL pipeline and includes **Bash-based automation and execution logging** using Git Bash.

## Project Overview

The pipeline takes raw customer shopping data, processes it through separate ETL stages, loads the cleaned data into MySQL, and records pipeline execution details in a log file.

```text
                    Raw CSV Data
                         │
                         ▼
                    ┌─────────┐
                    │ Extract │
                    └────┬────┘
                         │
                         ▼
                   ┌───────────┐
                   │ Transform │
                   └─────┬─────┘
                         │
                         ▼
                    Clean Data
                         │
                         ▼
                     ┌──────┐
                     │ Load │
                     └───┬──┘
                         │
                         ▼
                    MySQL Database
                         │
                         ▼
                    SQL Analysis


              Bash Automation
                     │
                     ▼
               main.py Pipeline
                     │
                     ▼
              logs/pipeline.log
```

## Tech Stack

* **Python**
* **Pandas**
* **MySQL**
* **SQLAlchemy**
* **PyMySQL**
* **python-dotenv**
* **Bash / Git Bash**
* **Git & GitHub**

## Project Structure

```text
customer_analysis_using_python_sql/
│
├── data/
│   ├── customer_shopping_behavior.csv
│   └── processed/
│       └── clean_customer_shopping_behavior.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── database.py
│   └── load.py
│
├── script/
│   └── run_pipeline.sh
│
├── logs/
│   └── pipeline.log
│
├── main.py
├── .gitignore
└── README.md
```

## ETL Pipeline

### 1. Extract

The `extract.py` module reads the raw customer shopping dataset using Pandas.

The raw data is loaded into a DataFrame and passed to the transformation stage.

### 2. Transform

The `transform.py` module handles data cleaning and transformation.

The process includes:

* Checking the dataset
* Handling missing review ratings
* Standardizing column names
* Renaming columns
* Creating customer age groups
* Converting purchase frequency into numerical values
* Removing unnecessary or redundant information

The cleaned data is then prepared for loading.

### 3. Save Processed Data

After transformation, the cleaned dataset is saved separately from the original raw data.

```text
data/processed/clean_customer_shopping_behavior.csv
```

Keeping the processed dataset separate helps preserve the original source data.

### 4. Load into MySQL

The `database.py` module manages the MySQL database connection.

The `load.py` module loads the transformed DataFrame into MySQL using SQLAlchemy.

The final table is:

```text
customer_purchase_data
```

Database credentials are stored using environment variables rather than being hard-coded in the Python files.

---

# Pipeline Automation

After building the ETL pipeline, I automated its execution using a **Bash script**.

The script is located at:

```text
script/run_pipeline.sh
```

It acts as a simple entry point for running the complete ETL pipeline.

### Automation Script

```bash
#!/bin/bash

echo "Pipeline started: $(date)" > logs/pipeline.log
python ../main.py >> logs/pipeline.log
echo "Pipeline finished: $(date)" >> logs/pipeline.log
```

Instead of manually running the Python pipeline every time, the Bash script executes `main.py` and records the execution information.

### Run the Pipeline

Using Git Bash:

```bash
./script/run_pipeline.sh
```

This starts the complete ETL process through the Bash script.

---

# Pipeline Logging

I also added basic logging to track pipeline execution.

The log file is:

```text
logs/pipeline.log
```

The script records:

* Pipeline start time
* Output generated while running the Python pipeline
* Pipeline completion time

Example:

```text
Pipeline started: Wed Sep 30 02:20:15 IST 2026
...
Pipeline finished: Wed Sep 30 02:20:18 IST 2026
```

The `>>` operator appends the Python pipeline output to the log file instead of displaying it only in the terminal.

### View the Logs

```bash
cat logs/pipeline.log
```

This makes it easy to verify whether the pipeline executed and when it started and finished.

---

# Why Automation and Logging?

The Bash automation provides a single command to execute the complete pipeline instead of manually running individual Python files.

Logging provides a simple execution record that can be checked later for:

* Pipeline execution time
* Successful completion
* Python output
* Basic troubleshooting

This also makes the project closer to a real-world data pipeline workflow where **automation, monitoring, and troubleshooting** are important parts of the process.

---

# Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Shubham1io/customer_analysis_using_python_sql.git

cd customer_analysis_using_python_sql
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install pandas sqlalchemy pymysql python-dotenv
```

### 4. Configure MySQL

Create the database:

```sql
CREATE DATABASE customer_analysis;
```

Create a `.env` file:

```env
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=customer_analysis
```

### 5. Run Through Bash Automation

Open Git Bash in the project directory and run:

```bash
./script/run_pipeline.sh
```

### 6. Check Pipeline Logs

```bash
cat logs/pipeline.log
```

---

# SQL Analysis

Once the data has been loaded into MySQL, SQL queries can be used to analyze customer purchasing behavior.

For example:

```sql
SELECT
    category,
    SUM(purchase_amount) AS total_purchase_amount
FROM customer_purchase_data
GROUP BY category
ORDER BY total_purchase_amount DESC;
```

Average review rating by category:

```sql
SELECT
    category,
    ROUND(AVG(review_rating), 2) AS average_rating
FROM customer_purchase_data
GROUP BY category
ORDER BY average_rating DESC;
```

---

# Key Learning Outcomes

Through this project, I gained hands-on experience with:

* Building a modular ETL pipeline
* Extracting data using Python and Pandas
* Cleaning and transforming data
* Feature engineering
* Saving processed datasets
* Connecting Python with MySQL
* Loading data into MySQL using SQLAlchemy
* Managing database credentials with environment variables
* Automating pipeline execution using Bash
* Working with Git Bash/Linux commands
* Creating and executing shell scripts
* Redirecting command output to log files
* Adding timestamps to pipeline logs
* Verifying pipeline execution through logs
* Using SQL for customer data analysis

---

# Future Improvements

* Add structured application logging
* Add error handling and failure logs
* Add data validation checks
* Schedule automated pipeline execution
* Add pipeline monitoring
* Containerize the pipeline using Docker
* Deploy the pipeline to AWS

---

# Author

**Shubham Kumar**

GitHub: https://github.com/Shubham1io
