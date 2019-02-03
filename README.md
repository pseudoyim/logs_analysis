# Project 1: Logs Analysis

This project uses Python and psycopg2 to query a mock PostgreSQL database for a fictional news website. The database has the following three tables:

- **articles**: Data on articles' author, title, slug, lead, body, time, and id.
- **authors**: Data on authors' names, bios, and id.
- **log**: Logged data of every instance of users' calls to the news website, including path, ip, method, status code, timestamp, and log id.

When executing the `analayze.py` script, queries are run that answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The results are printed to stdout in the terminal.


## Requirements

To run this program, you will need Python >=3.6, along with psycopg2 and PostgreSQL.


## Program design

The general design of this program (`analyze.py`) is as follows:

- Import statements
- SQL queries for each question
- Functions to run each query and format the output in Python


## How to run

1. Create and activate an environment (I recommend conda) with the following:

- `python >=3.6`
- `psycopg2`
- `postgresql` (if you don't already have this installed on your system)

2. Clone this repo and `cd` into it.

3. From the repo directory, download the [`newsdata.zip`](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file that will create your mock database.

4. Unzip the `newsdata.zip` file. Afterwards, you should have a `newsdata.sql` file.

5. Run this postgres command to create your database using the `newsdata.sql` file:
```
psql -d news -f newsdata.sql
```

6. Now run the Python script, which queries the database:
```
python analyze.py
```