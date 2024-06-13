SELECT
  "PUBLIC"."ORDERS"."USER_ID" AS "USER_ID",
  AVG("PUBLIC"."ORDERS"."TAX") AS "avg"
FROM
  "PUBLIC"."ORDERS"
GROUP BY
  "PUBLIC"."ORDERS"."USER_ID"
ORDER BY
  "PUBLIC"."ORDERS"."USER_ID" ASC