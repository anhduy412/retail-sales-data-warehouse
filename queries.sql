INSERT INTO fact_customer(discount_key)
SELECT dim_discount.discount_key
FROM dcscd
JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate AND dcscd.sales = dim_discount.sales