SELECT c.Name AS "Customers"
FROM Customers c
WHERE c.Id NOT IN 
    (SELECT Orders.CustomerId
    FROM Orders)