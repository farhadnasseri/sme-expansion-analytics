SELECT 
    Country, 
    Category, 
    COUNT(OrderID) AS Total_Orders,
    SUM(CASE WHEN IsReturned = 1 THEN 1 ELSE 0 END) AS Returned_Orders,
    ROUND(SUM(CASE WHEN IsReturned = 1 THEN 1.0 ELSE 0.0 END) / COUNT(OrderID) * 100, 2) AS Return_Rate_Percentage
FROM Transactions
GROUP BY 
    Country, 
    Category
ORDER BY 
    Return_Rate_Percentage DESC;