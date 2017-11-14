<h1>Project to query a database for</h1></br>
1 top three articles</br>
2 top actors</br>
3 day's with http failed request's greater then 1%</br>
</br>
To use view the query data</br>
1 clone this repo</br>
2 download the database</br>
<a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">database download</a></br>
3 save the database download in the directory of the cloned repo</br>
4 run this command to connect to the database this will also</br>
run the sql commands in newsdata.sql file</br>
$ psql -d news -f newsdata.sql</br>
5 create errorCount view in the news Database</br>
CREATE VIEW errorCount AS</br>
SELECT CAST(time AS DATE), COUNT(*)</br>
FROM log</br>
WHERE status!='200 OK'</br>
GROUP BY CAST(time AS DATE);</br>

6 create totalCount view in the news Database</br>
CREATE VIEW totalCount AS</br>
SELECT CAST(time AS DATE), COUNT(*)</br>
FROM log</br>
GROUP BY CAST(time AS DATE);</br>

7 run the command $ python data.py</br>
8 this will show the results of query's</br>
