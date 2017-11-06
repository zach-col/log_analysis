import psycopg2


def topThreeArticles():
    # query1 will select top 3 most popular articles
    query1 = '''SELECT articles.title, log.path, COUNT(*)
    FROM log join articles
    on articles.slug = substr(log.path, 10)
    GROUP BY articles.title, log.path
    ORDER BY COUNT DESC offset 1 limit 3;'''
    # Database name
    DBNAME = "news"
    # Connecting to database
    db = psycopg2.connect(database=DBNAME)
    # Creating cursor
    c = db.cursor()
    # Executing query
    c.execute(query1)
    # Fetching query
    queryData = c.fetchall()
    # Looping thru data
    print "Top Three Articles:"
    for data in queryData:
        print " Title: ", data[0], " Path: ", data[1]
    db.close()


def topActors():
    # query2 will select most popular authors"
    query2 = '''
    SELECT authors.name, COUNT(*) as views
    FROM ((log join articles
    on articles.slug = substr(log.path, 10))
    articles join authors on articles.author = authors.id)
    GROUP BY authors.name
    ORDER BY views DESC;
    '''
    # Database name
    DBNAME = "news"
    # Connecting to database
    db = psycopg2.connect(database=DBNAME)
    # Creating cursor
    c = db.cursor()
    # Executing query
    c.execute(query2)
    # Fetching data
    queryData = c.fetchall()
    # Looping thru data
    print "Top Three Articles:"
    for data in queryData:
        print " Author: ", data[0], " Views: ", data[1]

    db.close()


def topErrorDays():
    # query3 select days with request that are more then 1%
    query3 = '''
    Select totalCount.time,
    ROUND(CAST(errorCount.count AS float)/ totalCount.count * 100)
    FROM totalCount
    INNER JOIN errorCount ON totalCount.time = errorCount.time
    WHERE ROUND(CAST(errorCount.count AS float)/ totalCount.count * 100) > 1
    GROUP BY totalCount.time, errorCount.count, totalCount.count;
   '''
    # Database name
    DBNAME = "news"
    # Connecting to database
    db = psycopg2.connect(database=DBNAME)
    # Creating cursor
    c = db.cursor()
    # Executing query
    c.execute(query3)
    # Fetching data
    queryData = c.fetchall()
    # Looping thru data
    print "Top days with errors:"
    for data in queryData:
        print " Day", data[0], " Error: ", data[1], "%"

    db.close()

if __name__ == "__main__":
    topThreeArticles()
    topActors()
    topErrorDays()

