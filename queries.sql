SELECT * FROM [dbo].[category];
SELECT * FROM [dbo].[customer];
SELECT * FROM [dbo].[department];
SELECT * FROM [dbo].[orders];
SELECT * FROM [dbo].[product];
SELECT * FROM [dbo].[shipment];
SELECT * FROM [dbo].[store];
SELECT * FROM [dbo].[date];
SELECT * FROM [dbo].[benefit];
SELECT * FROM [dbo].[date];
SELECT * FROM [dbo].[sales];
SELECT * FROM [dbo].[sales_per_time];
SELECT * FROM [dbo].[dim_date];

SELECT fact_table.column1, dim_table1.column2, dim_table2.column3
FROM fact_table
INNER JOIN dim_table1
ON fact_table.dim_table1_id = dim_table1.dim_table1_id
INNER JOIN dim_table2
ON fact_table.dim_table2_id = dim_table2.dim_table2_id;

INSERT INTO fact_customer 
    SELECT
        customer_key,
        product_key
    FROM dcscd
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_key = dim_product.product_id

DROP TABLE fact_customer

CREATE TABLE test(
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
    )

INSERT INTO test(customer_key, product_key)
    SELECT
        customer_key,
        product_key
    FROM dcscd
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id

SELECT * FROM test