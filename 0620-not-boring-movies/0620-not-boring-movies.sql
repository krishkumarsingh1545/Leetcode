# Write your MySQL query statement below
SELECT * FROM Cinema
where description != 'boring' and ID % 2 != 0
ORDER BY rating DESC;