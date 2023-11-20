
def queries():
    """
    This function returns the queries used to retrieve
    :return:
    """
    query = {
        'top_25_terms': """
            SELECT term, ROUND(AVG(rank)) AS avg_rank, ROUND(AVG(score)) AS avg_score
            FROM `bigquery-public-data.google_trends.top_terms`
            WHERE refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL @num DAY)
            GROUP BY term
            ORDER BY 2 ASC
        """,
        'top_25_rising_terms': """
            SELECT term, ROUND(AVG(rank)) AS avg_rank, ROUND(AVG(score)) AS avg_score
            FROM `bigquery-public-data.google_trends.top_rising_terms`
            WHERE refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL @num DAY)
            GROUP BY term
            ORDER BY 2 ASC
        """,
        'top_25_international_terms': """
        SELECT  country_name AS country,
                term,
                ROUND(AVG(rank)) AS avg_rank,
                ROUND(AVG(score)) AS avg_score
        FROM `bigquery-public-data.google_trends.international_top_terms`
        WHERE   refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL @interval DAY)
                AND country_name = @country_name
        GROUP BY 1, 2
        ORDER BY 3 ASC
        """,
        'top_25_international_rising_terms': """
            SELECT  country_name AS country,
                    term, ROUND(AVG(rank)) AS avg_rank, ROUND(AVG(score)) AS avg_score
            FROM `bigquery-public-data.google_trends.top_rising_terms`
            WHERE refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL @interval DAY)
            AND country_name = @country_name
            GROUP BY 1, 2
            ORDER BY 3 ASC
        """,
        'top_25_terms_dma_name': """
            SELECT  term,
                    ROUND(AVG(rank)) AS avg_rank,
                    ROUND(AVG(score)) AS avg_score
            FROM `bigquery-public-data.google_trends.top_rising_terms`
            WHERE refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
            AND dma_name = @dma_name
            GROUP BY term
            ORDER BY 2 ASC
        """,
        'top_terms_international_country': """
            WITH ranked_terms AS
        (
          SELECT country_name AS country,
                 term,
                 ROUND(AVG(rank)) AS avg_rank,
                 ROUND(AVG(score)) AS avg_score,
                 DENSE_RANK() OVER (PARTITION BY country_name
                                    ORDER BY ROUND(AVG(rank)) ASC) AS rank_order
            FROM `bigquery-public-data.google_trends.international_top_terms`
            WHERE   refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL @interval DAY)
            GROUP BY 1, 2
            ORDER BY 3 ASC
        )
        SELECT  country, MAX(term) AS term,
                MAX(avg_rank) AS rank,
                MIN(avg_score) AS score
        FROM ranked_terms
        WHERE rank_order = 1
        GROUP BY country
        ORDER BY rank ASC, country;
        """,

    }

    return query
