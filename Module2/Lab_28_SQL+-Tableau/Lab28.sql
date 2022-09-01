CREATE PROCEDURE filter_salary (IN p_min_salary FLOAT, IN p_max_salary FLOAT)
BEGIN
DROP TABLE gender_salary
CREATE TABLE gender_salary AS (
SELECT e.gender, d.dept_name, AVG(s.salary) as avg_salary
FROM t_salaries s
JOIN employees e on s.emp_no = e.emp_no
JOIN dept_emp de on de.emp_no = e.emp_no
JOIN departments d on d.dept_no = de.dept_no
WHERE s.salary BETWEEN p_min_salary AND p_max_salary
GROUP BY d.dept_no, e.gender)
END$$
DELIMITER ;
CALL filter_salary(50000, 90000);