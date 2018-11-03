create database if not exists dsaa;
use dsaa;
create table test (id int(10) AUTO_INCREMENT ,address varchar(255), UNIQUE(address) , UNIQUE(id) );
