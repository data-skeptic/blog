## Using Cross Join Lateral for Improved JSON Handling in Postgres

Many data science courses and blogs cover the fun part of data science: designing machine (and deep) learning models for prediction. However, a precursor to the fun stuff is pulling the data from databases and preparing it for the machine learning algorithms we all love. 

In the course of a data scientist's (and analyst's) work, they will likely need to know how to work with JSON arrays and objects. This blog post will highlight a neat way to parse through a JSON array within PostreSQL (Postgres) using [`cross join lateral`](https://www.postgresql.org/docs/9.6/static/queries-table-expressions.html)  and [`jsonb_to_recordset()`](https://www.postgresql.org/docs/9.6/static/functions-json.html). The combination of these two functions together allows us to create a (mini) table that we can use to join, manipulate, and filter within our main Postgres query.

Before coming across these two functions, I frequently used `jsonb_array_elements()` combined with`->>`, which I found a bit more clunky, to parse and prepare JSON arrays. It often required using a [CTE](https://www.postgresql.org/docs/9.6/static/queries-with.html) statement or nesting a query within the FROM statement.

---

For the purposes of this post, let's use the table below written in Postgres. For ease in seeing the data structure, I set up a [SQL Fiddle](http://sqlfiddle.com/#!17/0fec9/22). 
```SQL
create table purchase_table (
    id serial primary key,
    customer_id text,
    purchase_date date,
    order_detail jsonb
);

insert into purchase_table values (
  ('13512559'), ('315'), ('2018-03-25'),
'[{
  "order_id": 123,
  "total_items": 4,
  "items": ["eggs","avocado", "bread", "salt"],
  "total_cost": "12.87",
  "gift_card": {
    "x": false
  }
 }]
'::jsonb);
insert into purchase_table values (
    ('13512671'), ('167'), ('2018-03-25'),
'[{
    "order_id": 98,
    "total_items": 2,
    "items": ["milk","coffee"],
    "total_cost": "9.29",
    "gift_card": {
      "x": true
    }
  }]
'::jsonb);
```

I don't want to spend too much time on the code creating our table, but in essence, we are looking at a table that has data on customer purchases. We have a column for the record ID (`id`), the customer ID (`customer_id`), the date the goods were purchased (`purchase_date`), and our last column which is a JSON array containing details of the order (`order_detail`).

*Our Table:*  

id | customer_id | purchase_date | order_detail 
--- | --- | --- | ---  
13512559 | 315 | 2018-03-25 | [{"items": ["eggs", "avocado", "bread", "salt"], "order_id": 123, "gift_card": {"x": false}, "total_cost": "12.87", "total_items": 4}] 
13512671 | 167 | 2018-03-25 | [{"items": ["milk", "coffee"], "order_id": 98, "gift_card": {"x": true}, "total_cost": "9.29", "total_items": 2}] 



### The Old Way
One way of parsing through this JSON array is using `jsonb_array_elements()` combined with`->>`. 
```SQL
WITH initial as (
  SELECT 
    customer_id, purchase_date, 
    jsonb_array_elements(order_detail) as order_detail
  FROM purchase_table
  )
select 
  customer_id, purchase_date,
  order_detail->>'order_id' as order_id,
  order_detail->>'items' as items,
  order_detail->>'total_cost' as total_cost,
  order_detail->>'total_items' as total_items
from initial
```

### The New Way
However, is there a way to get to the same outcome without using a CTE or nested FROM statement? Enter `jsonb_to_recordset()` and `CROSS JOIN LATERAL`! Let's start:
```SQL
SELECT 
  customer_id, purchase_date,
  od.order_id, od.total_items,
  od.items, od.total_cost, od.gift_card
FROM purchase_table
CROSS JOIN LATERAL jsonb_to_recordset(order_detail) 
  as od(
    order_id numeric,
    total_items numeric,
    items jsonb,
    total_cost float,
    gift_card jsonb
    )
```


*Parsed Table:*   

customer_id | purchase_date | order_id | total_items | items | total_cost | gift_card
--- | --- | --- | --- | --- | --- | --- 
315 | 2018-03-25 | 123 | 4 | ["eggs","avocado", "bread", "salt"] | 12.87 | "x": false
167 | 2018-03-25 | 98 | 2 | ["milk","coffee"] | 9.29 | "x": true



Now, let's break this down to understand what each part is doing.
`jsonb_to_recordset()` 'builds an arbitrary set of records from a JSON array of objects'. I usually describe this as "building a mini table that you can use". I name the table using `as od` and subsequently define the columns I want to pull and the column [types](https://www.postgresql.org/docs/9.6/static/datatype.html). This has created a temporary table with those columns that we can now use to join on our `purchase_table` data, which is what `CROSS JOIN LATERAL` helps us with.

---
### Additional Notes
#### Filtering
You also do not need to define each column within `order_detail`. If you only want the total_items and total_cost, you can easily signify that. Additionally, the combination of these functions allow for filtering within the same query rather than needing a CTE statement or nested FROM statement.

If you wanted only orders that had 3 or more items and were only interested in `total_items` and `total_cost`, your query would look as so:
```SQL 
SELECT 
  customer_id, purchase_date,
  od.total_items, od.total_cost
FROM purchase_table
CROSS JOIN LATERAL jsonb_to_recordset(order_detail) 
  as od(
    total_items numeric,
    total_cost float
    )
WHERE total_items >=3
```

customer_id | purchase_date | order_id | total_items | items | total_cost | gift_card
--- | --- | --- | --- | --- | --- | --- 
315 | 2018-03-25 | 123 | 4 | ["eggs","avocado", "bread", "salt"] | 12.87 | "x": false


#### Handling Camel Case
1. If your JSON array contains a string that is *camel case* (e.g., camelCase), then you will need to keep the camel case and wrap that variable in double quotes. Example: referencing the query code above, if `total_items` was actually `totalItems`, my query would look as followed:  
```SQL
SELECT 
  customer_id, purchase_date,
  od."totalItems", od.total_cost
FROM purchase_table
CROSS JOIN LATERAL jsonb_to_recordset(order_detail) 
  as od(
    "totalItems" numeric,
    total_cost float
    )
WHERE total_items >=3
``` 
#### Only one `CROSS JOIN LATERAL` per query
2. Using *two or more `CROSS JOIN LATERAL`'s* in this format within the same query could duplicate your data so it's best to use this when you only need to parse and prepare through a single JSON array.


So, there you have it! A new (and hopefully easier and helpful) way to use parse, join, and prepare your JSON data. Happy data-ing!
