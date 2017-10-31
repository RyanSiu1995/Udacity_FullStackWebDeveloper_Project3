import psycopg2 as psql


class Logs:
    def __init__(self, database):
        self.database = database
        self.connect = psql.connect("dbname=" + self.database)
        # Fetch the number of authors
        cursor = self.connect.cursor()
        cursor.execute(
            '''
            select count(*) from authors
            ''')
        self.authorNumber = cursor.fetchone()[0]
        # Fetch the number of articles
        cursor = self.connect.cursor()
        cursor.execute(
            '''
            select count(*) from articles
            ''')
        self.articleNumber = cursor.fetchone()[0]

    def popularArticles(self, number=None):
        # Set the default value of number of articles from self
        if not number:
            number = self.articleNumber
        cursor = self.connect.cursor()
        cursor.execute(
            '''
            select articles.title, count(log.path) as counting
            from articles join log on log.path = (%s) || articles.slug
            group by articles.title
            order by counting desc
            limit (%s)
            ''', ("/article/", number))
        return cursor.fetchall()

    def popularAuthors(self, number=None):
        # Set the default value of number of authors from self
        if not number:
            number = self.authorNumber
        cursor = self.connect.cursor()
        cursor.execute(
            '''
            select quicklook.name, count(log.path) as counting
            from (select authors.name, (%s) || articles.slug as url
            from authors right join articles
            on authors.id = articles.author) as quickLook left join log
            on log.path = quicklook.url
            group by quicklook.name
            order by counting desc
            limit (%s)
            ''', ("/article/", number))
        return cursor.fetchall()

    def errorReport(self):
        cursor = self.connect.cursor()
        cursor.execute(
            """
            select totalCount.day,
            errorRequest/totalRequest::float * 100 as errorPercentage
            from (select date_trunc('day', time) as day,
            count(status) as totalRequest
            from log
            group by day) as totalCount left join
            (select date_trunc('day', time) as day,
            count(status) as errorRequest
            from (select * from log where status like '%40%') as errorLog
            group by day) as errorCount
            on totalCount.day = errorCount.day
            where errorRequest/totalRequest::float * 100 > 1
            """)
        return cursor.fetchall()
