use master
select * into outfile "/var/lib/mysql-files/pageviews.csv" from pageview_counts order by title asc