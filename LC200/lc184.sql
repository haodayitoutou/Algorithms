SELECT D.Name AS "Department",
         E.Name AS "Employee",
         E.Salary
FROM Department D, Employee E, 
    (SELECT DepartmentId,
         MAX(Salary) AS "Salary"
    FROM Employee
    GROUP BY  DepartmentId) S
WHERE E.Salary = S.Salary
        AND E.DepartmentId = S.DepartmentId
        AND E.DepartmentId = D.Id