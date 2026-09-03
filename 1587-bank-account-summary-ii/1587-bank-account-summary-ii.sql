# Write your MySQL query statement below
SELECT
    u.name,
    sum(t.amount) AS balance
FROM Transactions AS t
JOIN Users AS u
    ON t.account = u.account
GROUP BY t.account, u.name
HAVING sum(t.amount) > 10000;