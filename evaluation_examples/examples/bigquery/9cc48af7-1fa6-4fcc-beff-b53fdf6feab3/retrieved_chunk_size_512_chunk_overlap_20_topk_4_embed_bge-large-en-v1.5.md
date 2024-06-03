Documentation Source:
cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls.md

Documentation Title:
Window function calls  |  BigQuery  |  Google Cloud

Documentation Content:
* (banana, **apple**, **leek**, **cabbage**, **lettuce**, **kale**) = 54 total purchases
* (**banana**, apple, **leek**, **cabbage**, **lettuce**, **kale**) = 54 total purchases
* (**banana**, **apple**, leek, **cabbage**, **lettuce**, **kale**) = 54 total purchases
* (**banana**, **apple**, **leek**, cabbage, **lettuce**, **kale**) = 54 total purchases
* (**banana**, **apple**, **leek**, **cabbage**, lettuce, **kale**) = 54 total purchases
* (**banana**, **apple**, **leek**, **cabbage**, **lettuce**, kale) = 54 total purchases

`SELECT item, purchases, category, SUM(purchases)
 OVER () AS total_purchases
FROM Produce

/*-------------------------------------------------------*
 | item | purchases | category | total_purchases |
 +-------------------------------------------------------+
 | banana | 2 | fruit | 54 |
 | leek | 2 | vegetable | 54 |
 | apple | 8 | fruit | 54 |
 | cabbage | 9 | vegetable | 54 |
 | lettuce | 10 | vegetable | 54 |
 | kale | 23 | vegetable | 54 |
 *-------------------------------------------------------*/`### Compute a subtotal

This computes a subtotal for each category in the
`Produce`table.



Documentation Source:
cloud.google.com/bigquery/docs/slots-autoscaling-intro.md

Documentation Title:
Introduction to slots autoscaling  |  BigQuery  |  Google Cloud

Documentation Content:
renewal or commercial migration). For example:
  +------------------------+------------------+--------------------+--------+------------+--------+-----------+----------------------------+
  |  change_timestamp   | capacity_commitment_id | commitment_plan | state  | slot_count | action | next_plan | next_plan_change_timestamp |
  +---------------------+------------------------+-----------------+--------+------------+--------+-----------+----------------------------+
  | 2023-07-20 19:30:27 | 12954109101902401697   | ANNUAL          | ACTIVE |        100 | CREATE | ANNUAL    |        2023-07-20 19:30:27 |
  | 2023-07-27 22:29:21 | 11445583810276646822   | FLEX            | ACTIVE |        100 | CREATE | FLEX      |        2023-07-27 22:29:21 |
  | 2023-07-27 23:10:06 | 7341455530498381779    | MONTHLY         | ACTIVE |        100 | CREATE | FLEX      |        2023-07-27 23:11:06 |
  | 2023-07-27 23:11:06 | 7341455530498381779    | FLEX            | ACTIVE |        100 | UPDATE | FLEX      |        2023-07-27 23:11:06 |
  */
  commitments_with_next_plan AS (
    SELECT
      *,
      IFNULL(
        LEAD(commitment_plan)
          OVER (
            PARTITION BY capacity_commitment_id ORDER BY change_timestamp ASC
          ),
        commitment_plan)
        next_plan,
      IFNULL(
        LEAD(change_timestamp)
          OVER (
            PARTITION BY capacity_commitment_id ORDER BY change_timestamp ASC
          ),
        change_timestamp)
        next_plan_change_timestamp
    FROM
      `region-us.INFORMATION_SCHEMA.CAPACITY_COMMITMENT_CHANGES_BY_PROJECT`
  ),

  /*
  Insert a 'DELETE' action for those with updated plans.



Documentation Source:
cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls.md

Documentation Title:
Window function calls  |  BigQuery  |  Google Cloud

Documentation Content:
The upper boundary is 1 row after the current row.

* (banana, **leek**, apple, cabbage, lettuce, kale) = 2 average purchases
* (**banana**, leek, **apple**, cabbage, lettuce, kale) = 4 average purchases
* (banana, **leek**, apple, **cabbage**, lettuce, kale) = 6.3333 average purchases
* (banana, leek, **apple**, cabbage, **lettuce**, kale) = 9 average purchases
* (banana, leek, apple, **cabbage**, lettuce, **kale**) = 14 average purchases
* (banana, leek, apple, cabbage, **lettuce**, kale) = 16.5 average purchases

`SELECT item, purchases, category, AVG(purchases)
 OVER (
 ORDER BY purchases
 ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
 ) AS avg_purchases
FROM Produce

/*-------------------------------------------------------*
 | item | purchases | category | avg_purchases |
 +-------------------------------------------------------+
 | banana | 2 | fruit | 2 |
 | leek | 2 | vegetable | 4 |
 | apple | 8 | fruit | 6.33333 |
 | cabbage | 9 | vegetable | 9 |
 | lettuce | 10 | vegetable | 14 |
 | kale | 23 | vegetable | 16.5 |
 *-------------------------------------------------------*/`### Compute the number of items within a range

This example gets the number of animals that have a similar population
count in the `Farm`table.

* (goose, **dog**, **ox**, **goat**, duck, cat) = 4 animals between population range 0-2.
* (**goose**, dog, **ox**, **goat**, **duck**, cat) = 5 animals between population range 1-3.
* (**goose**, **dog**, ox, **goat**, **duck**, cat) = 5 animals between population range 1-3.
* (**goose**, **dog**, **ox**, goat, **duck**, cat) = 5 animals between population range 1-3.



Documentation Source:
cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls.md

Documentation Title:
Window function calls  |  BigQuery  |  Google Cloud

Documentation Content:
The
`Produce`table is referenced.

* fruit
	+ (banana, **apple**) = apple is most popular
	+ (**banana**, apple) = apple is most popular
* vegetable
	+ (leek, **cabbage**, **lettuce**, **kale**) = kale is most popular
	+ (**leek**, cabbage, **lettuce**, **kale**) = kale is most popular
	+ (**leek**, **cabbage**, lettuce, **kale**) = kale is most popular
	+ (**leek**, **cabbage**, **lettuce**, kale) = kale is most popular

`SELECT item, purchases, category, LAST_VALUE(item)
 OVER (
 PARTITION BY category
 ORDER BY purchases
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
 ) AS most_popular
FROM Produce

/*----------------------------------------------------*
 | item | purchases | category | most_popular |
 +----------------------------------------------------+
 | banana | 2 | fruit | apple |
 | apple | 8 | fruit | apple |
 | leek | 2 | vegetable | kale |
 | cabbage | 9 | vegetable | kale |
 | lettuce | 10 | vegetable | kale |
 | kale | 23 | vegetable | kale |
 *----------------------------------------------------*/`### Get the last value in a range

This example gets the most popular item in a specific window frame, using
the `Produce`table. The window frame analyzes up to three
rows at a time. Take a close look at the `most_popular`column for vegetables.
Instead of getting the most popular item in a specific category, it gets the
most popular item in a specific range in that category.



