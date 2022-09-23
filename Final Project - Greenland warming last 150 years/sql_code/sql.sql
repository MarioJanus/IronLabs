use greenland;
CREATE TABLE west1 (
	`index` int,
    Year int,
    Jan int,
    Feb int,
    Mar int,
    Apr int,
    May int,
    Jun int,
    Jul int,
    Aug int,
    Sept int,
    Oct int,
    Nov int,
    Dez int);

CREATE TABLE west2 (
	`index` int,
    Year int,
    Jan int,
    Feb int,
    Mar int,
    Apr int,
    May int,
    Jun int,
    Jul int,
    Aug int,
    Sept int,
    Oct int,
    Nov int,
    Dez int);
    
CREATE TABLE south1 (
	`index` int,
    Year int,
    Jan int,
    Feb int,
    Mar int,
    Apr int,
    May int,
    Jun int,
    Jul int,
    Aug int,
    Sept int,
    Oct int,
    Nov int,
    Dez int);

select * from west2;
SELECT Jan FROM west1 WHERE Year=1990;
SELECT Year, AVG(Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sept+Oct+Nov+Dez) FROM west1 
          WHERE Year>=1873 and Year<1893 GROUP BY Year;
          SELECT Year, SUM(Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sept+Oct+Nov+Dez)/12 as Year_Avg;
SELECT Year, SUM(Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sept+Oct+Nov+Dez)/12 as Year_Avg
        FROM west1;
        



SELECT CASE
         WHEN Year >= 1873 AND Year < 1893 THEN '1873-1892'
         WHEN Year >= 1893 AND Year < 1913 THEN '1893-1912'
         WHEN Year >= 1913 AND Year < 1933 THEN '1913-1932'
         WHEN Year >= 1933 AND Year < 1953 THEN '1933-1952'
         WHEN Year >= 1953 AND Year < 1973 THEN '1953-1972'
         WHEN Year >= 1973 AND Year < 1993 THEN '1973-1992'
         WHEN Year >= 1993 AND Year <= 2013 THEN '1993-2013'
       END,
       Count(*)
FROM   west1
WHERE  Year = 'Year'
       AND Year > 1873
       AND Year <= 2013
GROUP  BY CASE
		 WHEN Year >= 1873 AND Year < 1893 THEN '1873-1892'
         WHEN Year >= 1893 AND Year < 1913 THEN '1893-1912'
         WHEN Year >= 1913 AND Year < 1933 THEN'1913-1932'
         WHEN Year >= 1933 AND Year < 1953 THEN '1933-1952'
         WHEN Year >= 1953 AND Year < 1973 THEN '1953-1972'
         WHEN Year >= 1973 AND Year < 1993 THEN '1973-1992'
         WHEN Year >= 1993 AND Year <= 2013 THEN '1993-2013'
END;

