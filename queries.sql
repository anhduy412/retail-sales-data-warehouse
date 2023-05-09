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