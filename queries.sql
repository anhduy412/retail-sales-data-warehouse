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

SELECT * FROM fact_sales

    INSERT INTO fact_sales(order_key, date_key, customer_key, product_key, department_key, discount_key, order_item_quantity, order_item_total)
    SELECT
        dim_orders.order_key,
        dim_date.date_key,
        dim_customer.customer_key,
        dim_product.product_key,
        dim_department.department_key,
        dim_discount.discount_key
        order_item_quantity, 
        order_item_total
    FROM dcscd
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    JOIN dim_department ON dcscd.department_id = dim_department.department_id
    JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate AND dcscd.sales = dim_discount.sales


CREATE TABLE fact_sales(
        order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        category_key INT FOREIGN KEY REFERENCES dim_category(category_key),
        department_key INT FOREIGN KEY REFERENCES dim_department(department_key),
        discount_key INT FOREIGN KEY REFERENCES dim_discount(discount_key),
        shipment_key INT FOREIGN KEY REFERENCES dim_shipment(shipment_key),
        order_item_quantity INT,
        order_item_total FLOAT
)

INSERT INTO fact_sales(order_key, date_key, customer_key, product_key, category_key, department_key, shipment_key, order_item_quantity, order_item_total)
SELECT
    dim_orders.order_key,
    dim_date.date_key,
    dim_customer.customer_key,
    dim_product.product_key,
    dim_category.category_key,
    dim_department.department_key,
    dim_shipment.shipment_key,
    order_item_quantity, 
    order_item_total
FROM dcscd
JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
JOIN dim_category ON dcscd.category_id = dim_category.category_id
JOIN dim_department ON dcscd.department_id = dim_department.department_id
JOIN dim_shipment ON dcscd.days_for_shipment_scheduled = dim_shipment.days_for_shipment_scheduled AND dcscd.days_for_shipping_real = dim_shipment.days_for_shipping_real AND dcscd.shipping_date_dateorders = dim_shipment.shipping_date_dateorders AND dcscd.shipping_mode = dim_shipment.shipping_mode

DROP TABLE fact_sales

SELECT * FROM dim_discount
SELECT order_item_discount, order_item_discount_rate FROM dcscd

INSERT INTO fact_sales(order_key, date_key, customer_key, product_key, category_key, department_key, shipment_key, order_item_quantity, order_item_total)
    SELECT
        dim_orders.order_key,
        dim_date.date_key,
        dim_customer.customer_key,
        dim_product.product_key,
        dim_category.category_key,
        dim_department.department_key,
        dim_shipment.shipment_key,
        order_item_quantity, 
        order_item_total
    FROM dcscd
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    JOIN dim_category ON dcscd.category_id = dim_category.category_id
    JOIN dim_department ON dcscd.department_id = dim_department.department_id
    JOIN dim_shipment ON dcscd.days_for_shipment_scheduled = dim_shipment.days_for_shipment_scheduled AND dcscd.days_for_shipping_real = dim_shipment.days_for_shipping_real AND dcscd.shipping_date_dateorders = dim_shipment.shipping_date_dateorders AND dcscd.shipping_mode = dim_shipment.shipping_mode
INSERT INTO fact_sales(store_key)
SELECT 
    dim_store.store_key 
FROM dcscd_store
JOIN dim_store ON dcscd_store.latitude = dim_store.latitude AND dcscd_store.longitude = dim_store.longitude
INSERT INTO fact_sales(discount_key)
SELECT 
    dim_discount.discount_key 
FROM dcscd_discount
JOIN dim_discount ON dcscd.discount_order_item_discount = dim_discount.discount_order_item_discount AND dcscd.discount_rate = dim_discount.discount_rate