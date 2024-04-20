WITH happiness_data AS (
  SELECT
    AVG(CASE WHEN observation_year >= 2019 THEN bird_happiness END) AS avg_happiness_post_2019,
    AVG(CASE WHEN observation_year < 2019 THEN bird_happiness END) AS avg_happiness_pre_2019
  FROM '{{ params.table_name }}'
)
SELECT CASE
  WHEN avg_happiness_post_2019 < avg_happiness_pre_2019 THEN 1
  ELSE 0
END AS happiness_comparison
FROM '{{ params.table_name }}' JOIN happiness_data;

