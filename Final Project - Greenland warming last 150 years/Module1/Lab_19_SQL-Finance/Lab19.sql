select track_name, user_rating, rating_count_tot from applestore 
GROUP by track_name
order by user_rating desc, rating_count_tot desc
limit 3;

use olist;

select product_id,customers min(price)  from order_items;
select product_id, max(price)  from order_items;

select min(shipping_limit_date) MinDate, max(shipping_limit_date) MaxDate
FROM order_items

select customer_state, count(customer_state) from customers 
GROUP by customer_state
order by count(customer_state) desc
limit 1;

select customer_state, count(customer_city), customer_city from customers 
GROUP by customer_city
order by count(customer_city) desc
limit 1;

select business_segment from closed_deals
GROUP by business_segment;

select sum(declared_monthly_revenue) from closed_deals;

select business_segment, sum(declared_monthly_revenue)  from closed_deals
group by business_segment
order by sum(declared_monthly_revenue) desc
limit 3;

select review_score, count(review_score) from order_reviews
group by review_score;

ALTER TABLE order_reviews
ADD rev_name char(20);



select * from order_reviews