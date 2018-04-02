--
-- Tested on SQLite
--
-- Create DB: sqlite3 q2.db < q2-create.sql
-- Run query: sqlite3 q2.db < q2.sql
--
-- Galvanize Data Scientist application:
-- https://app.formassembly.com/418492?contactID=0030a00001uKYRI&tfa_14=a0K0a00000hWuNa
--
-- Repo: https://github.com/avibrazil/Galvanize-Data-Science-Acceptance

SELECT s.name, 
       sum(o.amount) 
FROM   salesperson s, 
       orders o 
WHERE  s.id = o.salesperson_id 
GROUP  BY o.salesperson_id 
HAVING sum(o.amount) > 1300;