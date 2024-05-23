SELECT
    orders.user_id              AS id,
    people.created_at           AS join_date,
    people.state                AS state,
    people.source               AS source,
    Sum(orders.total)           AS total,
    Count(*)                    AS order_count,
    Sum(orders.total)/Count(*)  AS avg_total
FROM orders
LEFT JOIN people
   ON orders.user_id = people.id
GROUP  BY
    id,
    city,
    state,
    zip,
    source
