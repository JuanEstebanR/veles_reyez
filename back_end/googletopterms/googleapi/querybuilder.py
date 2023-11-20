"""
This module contains the QueryBuilder class, which is used to build a query
"""
import os
import json
import pprint
from google.cloud import bigquery
from .google_queries import queries
"""
This module contains the queries used to retrieve
data from the Google Trends
"""
query = queries()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./google_service.json"

client = bigquery.Client()


def data_cleaning_top_terms_and_rising(result):
    """
    This function returns the data cleaned for the top terms based in the U.S.
    :return:
    """
    data = []
    for row in result:
        data.append({
            'term': row.term,
            'avg_rank': row.avg_rank,
            'avg_score': row.avg_score
        })
    return data


def data_cleaning_international_terms(result):
    """
    This function returns the data cleaned for the top terms based in the U.S.
    :return:
    """
    data = []
    for row in result:
        data.append({
            'country': row.country,
            'term': row.term,
            'avg_rank': row.avg_rank,
            'avg_score': row.avg_score
        })
    return data


def convert_to_json(result):
    """
    This function returns the data cleaned for the top terms based in the U.S.
    :return:
    """
    json_string = json.dumps(result)
    json_string = json.loads(json_string)
    return json_string


def top_25_terms_and_rising(table_name: str, interval: int):
    """
    This function returns the query for the top terms based in the U.S.
    :return:
    """
    if table_name == 'top_terms':
        raw_query = query['top_25_terms']
    else:
        raw_query = query['top_25_rising_terms']

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("num", "INT64", interval),
        ]
    )
    query_job = client.query(raw_query, job_config=job_config)
    data = data_cleaning_top_terms_and_rising(query_job.result())
    return raw_query, convert_to_json(data)


def top_25_international_terms_and_rising(table_name: str, country_name: str,
                                          interval: int):
    """
    This function returns the query for the top international terms based country name.
    :return:
    """
    if table_name == 'international_top_terms':
        raw_query = query['top_25_international_terms']
    else:
        raw_query = query['top_25_international_rising_terms']

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("interval", "INT64", interval),
            bigquery.ScalarQueryParameter("country_name", "STRING",
                                          country_name.strip().capitalize()),
        ]
    )
    query_job = client.query(raw_query, job_config=job_config)
    data = data_cleaning_international_terms(query_job.result())
    return raw_query, data


def top_international_terms(interval: int):
    """
    This function returns the query for the top 1 for each country in the
    international terms.
    :return:
    """
    raw_query = query['top_terms_international_country']
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("interval", "INT64", interval),
        ]
    )
    query_job = client.query(raw_query, job_config=job_config)
    return raw_query, query_job.result()
