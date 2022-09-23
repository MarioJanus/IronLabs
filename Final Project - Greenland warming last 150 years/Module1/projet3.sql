SELECT * FROM project3.data_cleaned;
### Repartition  willing
select TargetEntCompetency as "Target competency", round((count(TargetEntCompetency)/219)*100) as "% total" from data_cleaned
group by TargetEntCompetency;


#Répartition par domaine d'étude
select EducationSector as "Education sector", round((count(EducationSector)/219)*100) as  "% education sector" from data_cleaned
group by EducationSector
order by count(EducationSector)/219 desc;
# more than half of the sample is composed by student from engineering sector

select EducationSector as "Education sector", count(EducationSector) as "total per education sector" from data_cleaned
where TargetEntCompetency=0
group by EducationSector
order by count(EducationSector) desc;
 
 
 #répartition par genre
 select Gender , count(Gender) as "Total" from data_cleaned
 group by Gender;
 
 # répartition par genre ayant créait
 
select Gender , count(Gender) as "Total" from data_cleaned
where TargetEntCompetency=1
 group by Gender;
 
drop table ratio_per_gender;

select Gender, round((count(Gender)/57)*100) as "% female" from data_cleaned
where TargetEntCompetency=1 and Gender = "female";

select Gender, round((count(Gender)/162)*100) as "% male" from data_cleaned
where TargetEntCompetency=1 and Gender = "male";

select Influenced, round((count(TargetEntCompetency)/101)*100) as " % total" from data_cleaned
where TargetEntCompetency=1
group by Influenced;

###Mental disorder

select MentalDisorder as "Mental disorder" , count(TargetEntCompetency) as "total" from data_cleaned
group by MentalDisorder;  

select MentalDisorder as "Mental disorder" , count(TargetEntCompetency)  as "Total" from data_cleaned
where TargetEntCompetency=1
group by MentalDisorder;

select MentalDisorder as "Mental disorder" , count(TargetEntCompetency)  as " Total" from data_cleaned
where TargetEntCompetency=0
group by MentalDisorder;

### Desire to take initiative
select  DesireToTakeInitiative as "Desire to take initiative", count(DesireToTakeInitiative) as "Total positive" from data_cleaned
where TargetEntCompetency=1
group by DesireToTakeInitiative;

select  DesireToTakeInitiative as "Desire to take initiative", count(DesireToTakeInitiative) as "Total negative" from data_cleaned
where TargetEntCompetency=0
group by DesireToTakeInitiative;


#### key traits
select KeyTraits as "Key traits", count(KeyTraits) as "Total" from data_cleaned
where TargetEntCompetency=1
group by KeyTraits;

### self reliance
select SelfReliance  as "self reliance", count(SelfReliance) as "Total" from data_cleaned
where TargetEntCompetency=1
group by SelfReliance;

### Competitivness

select Competitiveness , count(Competitiveness) as "Total" from data_cleaned
where TargetEntCompetency=1
group by Competitiveness;
 
 ###Perseverance
 select Perseverance , count(Perseverance) as "Total" from data_cleaned
where TargetEntCompetency=1
group by Perseverance;

