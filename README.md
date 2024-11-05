Data Processing and SQL Assessment Project


Description

This project consists of various files related to a technical assessment involving customer data processing, SQL queries, and a data platform technical evaluation. The main goal of this project is to process customer information, including generating country abbreviations and integrating various data dimensions.

The project contains several files, each serving a unique purpose:

customer_dimension_with_abbreviations.csv: Contains customer data along with country abbreviations.

country_abbreviation.py: Python script to generate country abbreviations based on country names.

Intuit SQL Assessment Solution.png: Screenshot of the SQL solution for the assessment.

Inuit SQL Assessment Solution.csv: CSV file containing the SQL assessment solution data.

Inuit SQL Assessment Solution.sql: SQL script for solving the given SQL problem in the assessment.

emails_sent_fact.csv: Fact table containing email-related data.

date_dimension.csv: Date dimension data for time-based analysis.

customer_dimension.csv: Customer dimension data, typically used for data warehousing.

Data Platform Technical Assessment (1) (1) (1).pdf: PDF file containing the technical assessment instructions and details.


Requirements

Prerequisites

Python 3.x
SQL client (e.g., MySQL, PostgreSQL, or SQLite for running .sql files)
Libraries: pandas (for Python script)

Libraries
pandas: For handling CSV files and data manipulation.
To install required libraries, run:

	pip install pandas
 
Files Overview
1. customer_dimension_with_abbreviations.csv
Contains the customer dimension data along with country abbreviations.
2. country_abbreviation.py
Python script used for generating country abbreviations based on country names from customer data.
3. Intuit SQL Assessment Solution.png
A visual screenshot of the SQL solution that was used during the assessment.
4. Inuit SQL Assessment Solution.csv
CSV file containing the data solution for the SQL assessment problem.
5. Inuit SQL Assessment Solution.sql
SQL script to solve the SQL problem posed in the assessment. This script processes the customer and email data.
6. emails_sent_fact.csv
A fact table related to emails sent, likely used in the data warehouse for analysis.
7. date_dimension.csv
A date dimension table typically used for time-based analysis, such as sales or event tracking.
8. customer_dimension.csv
A customer dimension table, usually in a data warehouse for customer-centric analysis.
9. Data Platform Technical Assessment (1) (1) (1).pdf
A PDF file containing the technical assessment instructions and explanation of the tasks completed.

Setup

1. Clone the Repository
Clone the repository to your local machine:
	
 	git clone <repository_url>
	cd <repository_directory>
 
3. Install Dependencies
If you don't have a requirements.txt file, install the required Python libraries manually:

	pip install pandas

1. Running the Python Script (country_abbreviation.py)
You can run the country_abbreviation.py script to generate country abbreviations for customer data. The script reads the customer_dimension.csv file and generates the abbreviations based on the country names.

Run the Python script using:

	python country_abbreviation.py
 
The script will create a new file, customer_dimension_with_abbreviations.csv, which contains the original customer data along with the country abbreviations.

2. SQL Assessment
You can run the SQL script (Inuit SQL Assessment Solution.sql) in your preferred SQL client (e.g., MySQL, PostgreSQL) to execute the SQL solution. This file processes data and generates results as expected from the assessment.

To run the SQL:

Open the SQL file in your SQL client.
Execute the query to manipulate the customer and email data.
Refer to Inuit SQL Assessment Solution.csv for the output of the SQL query.
File Structure

	/repository
  	├── customer_dimension_with_abbreviations.csv   # Output file with country abbreviations added
  	├── country_abbreviation.py                    # Python script to generate country abbreviations
  	├── Intuit SQL Assessment Solution.png          # Screenshot of SQL solution
  	├── Inuit SQL Assessment Solution.csv          # CSV with SQL solution results
  	├── Inuit SQL Assessment Solution.sql          # SQL script for solving the assessment problem
  	├── emails_sent_fact.csv                       # Fact table for email data
  	├── date_dimension.csv                         # Date dimension table for time-based analysis
  	├── customer_dimension.csv                     # Customer dimension data
  	└── Data Platform Technical Assessment (1) (1) (1).pdf # PDF with technical assessment instructions
   
Contributing

1. Fork the repository.
2. Create a new branch for your changes (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a pull request.
