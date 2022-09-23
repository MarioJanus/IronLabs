![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)
# Lab | MySQL Select

## Introduction

 In this lab, we will practice selecting and projecting data. You can finish all questions with only these clauses:
- `SELECT`
- `SELECT DISTINCT`
- `COUNT`
- `FROM`
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `SUM`
- `LIMIT`

The Sql script is here: https://drive.google.com/file/d/1tT1OTdIgkI5tkeeXIsnZwMC5SxI1FE9m/view
Please submit your solutions in a text file `solutions.sql`.

#### 1. From the `order_items` table, find the price of the highest priced order and lowest price order.
00010242fe8c5a6d1ba2dd792cb16214	6735


#### 2. From the `order_items` table, what is range of the shipping_limit_date of the orders?
2016-10-10 13:43:22	2018-09-04 01:45:08

#### 3. From the `customers` table, find the states with the greatest number of customers.
SP	41746

#### 4. From the `customers` table, within the state with the greatest number of customers, find the cities with the greatest number of customers.
SP	15540	sao paulo


#### 5. From the `closed_deals` table, how many distinct business segments are there (not including null)?
air_conditioning
audio_video_electronics
baby
bags_backpacks
bed_bath_table
books
car_accessories
computers
construction_tools_house_garden
fashion_accessories
food_drink
food_supplement
games_consoles
gifts
handcrafted
health_beauty
home_appliances
home_decor
home_office_furniture
household_utilities
jewerly
music_instruments
other
party
perfume
pet
phone_mobile
religious
small_appliances
sports_leisure
stationery
toys
watches


#### 6. From the `closed_deals` table, sum the declared_monthly_revenue for duplicate row values in business_segment and find the 3 business segments with the highest declared monthly revenue (of those that declared revenue).
construction_tools_house_garden	50695006
phone_mobile	8000000
home_decor	710000

#### 7. From the `order_reviews` table, find the total number of distinct review score values.
1	11858
2	3235
3	8287
4	19200
5	57420


#### 8. In the `order_reviews` table, create a new column with a description that corresponds to each number category for each review score from 1 - 5, then find the review score and category occurring most frequently in the table.


#### 9. From the `order_reviews` table, find the review value occurring most frequently and how many times it occurs.

