SELECT d.Name "Department",
         e1.Name "Employee",
         e1.Salary
FROM Employee e1, Department d
WHERE 
    (SELECT COUNT(DISTINCT(e2.Salary))
    FROM Employee e2
    WHERE e2.DepartmentId = e1.DepartmentId
            AND e2.Salary > e1.Salary) < 3
        AND e1.DepartmentId = d.Id
ORDER BY  e1.DepartmentId, e1.Salary DESC; 