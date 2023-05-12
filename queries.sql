INSERT INTO fact_customer(customer_key, date_key, product_key, date_key, type, order_item_quantity, order_item_total)
SELECT
	dim_customer.customer_key,
	dim_product.product_key,
	date_key,
	type,
	order_item_quantity,
	order_item_total
FROM dcscd
JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
JOIN dim_date ON dcscd.order_date_dateorders = dim_date.[day]
JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate AND dcscd.sales = dim_discount.sales


INSERT INTO fact_sales(order_key, date_key, customer_key, product_key, order_item_quantity, order_item_total)
    SELECT
        dim_orders.order_key,
        dim_date.date_key,
        dim_customer.customer_key,
        dim_product.product_key,
        -- dim_discount.discount_key,
        order_item_quantity, 
        order_item_total
    FROM dcscd
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    -- JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate AND dcscd.sales = dim_discount.sales

SELECT * FROM fact_sales