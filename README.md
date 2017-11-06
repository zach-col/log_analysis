<h1>Project to query a database for</h1></br>
1 top three articles</br>
2 top actors</br>
3 day's with http failed request's greater then 1%</br>
</br>
To use the query's</br>
1 download data.py</br>
2 create errorCount view in the news Database</br>
CREATE VIEW errorCount AS</br>
SELECT CAST(time AS DATE), COUNT(*)</br>
FROM log</br>
WHERE status!='200 OK'</br>
GROUP BY CAST(time AS DATE);</br>

4 create totalCount view in the news Database</br>
CREATE VIEW totalCount AS</br>
SELECT CAST(time AS DATE), COUNT(*)</br>
FROM log</br>
GROUP BY CAST(time AS DATE);</br>

5 run the command $ python data.py</br>
6 this will show the results of query's</br>
