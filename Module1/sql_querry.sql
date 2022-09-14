use competency;
select * from data_cleaned;
select TargetEntCompetency, count(case when gender='female' then 1 end) as 'Female Want To Find Job', 
count(case when gender='male' then 1 end) as 'Male Want To Find Job'
from data_cleaned
group by TargetEntCompetency;

select TargetEntCompetency, count(case when gender='female' then 1 end) as female_cnt, 
count(case when gender='male' then 1 end) as male_cnt
from data_cleaned
group by TargetEntCompetency;


select Age, count(case when TargetEntCompetency=1 then 1 end) as 'Want to be Enterpreneur',
count(case when TargetEntCompetency=0 then 1 end) as 'Dont Want to be Enterpreneur'
from data_cleaned
group by age
order by TargetEntCompetency;

select MentalDisorder,
count(case when gender='female' then 1 end) as female_cnt, 
count(case when gender='male' then 1 end) as male_cnt 
 from data_cleaned
group by MentalDisorder

