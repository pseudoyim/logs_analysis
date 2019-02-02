#!/usr/bin/env python3

import datetime
import psycopg2

# Question 1: What are the most popular three articles of all time?
query_1 = '''
	SELECT 
		articles.title
		, COUNT(articles.title) AS accessed_count
	FROM (
		SELECT 
			id
			, SPLIT_PART(path, '/', 3) AS path 
		FROM log) AS log_with_path
	LEFT JOIN articles
		ON log_with_path.path = articles.slug
	GROUP BY articles.title
	ORDER BY accessed_count DESC
	LIMIT 3;
'''

"""Question 2: Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written, 
which authors get the most page views? Present this as a sorted list with 
the most popular author at the top.""" 
query_2 = '''
	SELECT
		COALESCE(authors.name, 'Anonymous Contributor')
		, COUNT(authors.name) AS accessed_count
	FROM (
		SELECT 
			id
			, SPLIT_PART(path, '/', 3) AS path 
		FROM log) AS log_with_path
	LEFT JOIN articles
		ON log_with_path.path = articles.slug
	LEFT JOIN authors
		ON articles.author = authors.id
	GROUP BY authors.name
	ORDER BY accessed_count DESC
	LIMIT 10;
'''

# Question 3: On which days did more than 1% of requests lead to errors?
query_3 = '''
	SELECT 
		date
		, SUM(is_error) / SUM(logged)::FLOAT AS error_pct
	FROM (SELECT 
			time::timestamp::date AS date
			, status
			, CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END AS is_error
			, 1 as logged
			FROM log) AS error_counts
	GROUP BY date
	HAVING SUM(is_error) / SUM(logged)::FLOAT > 0.01;
'''

def execute(query):
	cur.execute(query)
	output = cur.fetchall()
	return output


def run_query_1():
	output = execute(query_1)
	print('\nTop 3 Most Popular Articles (all time):')
	for item in output:
		print(f'"{item[0]}" - {item[1]} views')


def run_query_2():
	output = execute(query_2)
	print('\nMost Popular Article Authors (all time):')
	for item in output:
		print(f'{item[0]} - {item[1]} views')


def run_query_3():
	output = execute(query_3)
	print('\nDays when more than 1% of requests led to errors:')
	for item in output:
		date = item[0]
		date_formatted = date.strftime('%B %d, %Y')
		print(f'{date_formatted} - {round(item[1]*100, 2)}% errors')


def main():
	run_query_1()
	run_query_2()
	run_query_3()


if __name__ == '__main__':
	# Connect to an existing database
	conn = psycopg2.connect("dbname='news'")
	# Open a cursor to perform database operations
	cur = conn.cursor()
	# Run queries
	main()
	# Close communication with the database
	cur.close()
	conn.close()
