SELECT * FROM [dbo].[DataCoSupplyChainDataset]

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    calendar_date DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    day_of_week INT NOT NULL,
    day_of_year INT NOT NULL
);

INSERT INTO dim_date (date_key, calendar_date, year, quarter, month, day, day_of_week, day_of_year) 
SELECT 
    YEAR(calendar_date) * 10000 + MONTH(calendar_date) * 100 + DAY(calendar_date) AS date_key,
    calendar_date,
    YEAR(calendar_date) AS year,
    QUARTER(calendar_date) AS quarter,
    MONTH(calendar_date) AS month,
    DAY(calendar_date) AS day,
    WEEKDAY(calendar_date) + 1 AS day_of_week,
    DAYOFYEAR(calendar_date) AS day_of_year
FROM 
    (
        SELECT 
            DATE('2020-01-01') + INTERVAL (a.num * 10000 + b.num * 100 + c.num) DAY AS calendar_date 
        FROM 
            (SELECT 0 AS num UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) AS a,
            (SELECT 0 AS num UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) AS b,
            (SELECT 0 AS num UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9) AS c
    ) a
WHERE 
    calendar_date BETWEEN '2020-01-01' AND '2030-12-31';