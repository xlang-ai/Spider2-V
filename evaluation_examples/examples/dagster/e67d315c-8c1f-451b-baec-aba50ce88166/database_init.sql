create user 'user'@'localhost' identified by 'password';
grant select, reload, show databases, replication slave, replication client on *.* to 'user'@'localhost' with grant option;
flush privileges;

create database master;
use master;

create table pageview_counts (title varchar(255), views int, datetime varchar(255));

insert into pageview_counts values("Amazon", 7, "2024050208");
insert into pageview_counts values("Apple", 46, "2024050208");
insert into pageview_counts values("Facebook", 763, "2024050208");
insert into pageview_counts values("Google", 747, "2024050208");
insert into pageview_counts values("Microsoft", 190, "2024050208");
