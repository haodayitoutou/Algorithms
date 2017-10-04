DELETE
FROM Person
WHERE Id NOT IN 
    (SELECT t.Id
    FROM 
        (SELECT MIN(Id)
        FROM Person
        GROUP BY  Email) t )