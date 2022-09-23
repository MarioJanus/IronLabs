create database gender;
use gender;

insert into country (country_id, name)
values 
(1, "Argentina"),
(2, "Brazil"),
(3, "Chile"),
(4, "Ecuador"),
(5, "Venezuela");

ALTER TABLE pop_m RENAME COLUMN economy TO eco_pop_m;
ALTER TABLE pop_f RENAME COLUMN economy TO eco_pop_f;
ALTER TABLE mort_m RENAME COLUMN economy TO eco_mort_m;
ALTER TABLE mort_f RENAME COLUMN economy TO eco_mort_f;
ALTER TABLE emp_m RENAME COLUMN economy TO eco_emp_m;
ALTER TABLE emp_f RENAME COLUMN economy TO eco_emp_f;


create table pop_all as
select pop_f.*, pop_m.* from pop_f
inner join pop_m
on pop_f.eco_pop_f=pop_m.eco_pop_m;

create table emp_all as
select emp_f.*, emp_m.* from emp_f
inner join emp_m
on emp_f.eco_emp_f=emp_m.eco_emp_m;

create table mort_all as
select mort_f.*, mort_m.* from mort_f
inner join mort_m
on mort_f.eco_mort_f=mort_m.eco_mort_m;

ALTER TABLE emp_all
  DROP COLUMN eco_emp_m;
  
ALTER TABLE pop_all
  DROP COLUMN eco_pop_m;

ALTER TABLE mort_all
  DROP COLUMN eco_mort_m;  
  
ALTER TABLE emp_all RENAME COLUMN eco_emp_f TO eco_emp;
ALTER TABLE mort_all RENAME COLUMN eco_mort_f TO eco_mort;
ALTER TABLE pop_all RENAME COLUMN eco_pop_f TO eco_pop;

select * from emp_all