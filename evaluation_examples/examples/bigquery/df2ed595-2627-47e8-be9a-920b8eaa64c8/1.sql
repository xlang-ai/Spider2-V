SELECT 
  column_name,
  column_default
FROM `{}.census.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = '2012';
