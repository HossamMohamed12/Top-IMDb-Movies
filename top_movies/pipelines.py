import sqlite3


class TopMoviesPipeline:
    def process_item(self, item, spider):
        return item


class SaveToDatabasePipeline:
    def __init__(self):
        ## Create/Connect to database
        self.con = sqlite3.connect('movies.db')

        ## Create cursor, used to execute commands
        self.cur = self.con.cursor()

        ## Create quotes table if none exists
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS movies(
                rank INTEGER PRIMARY KEY,
                title TEXT,
                genres TEXT,
                release_date INTEGER,
                age_rating TEXT,
                duration TEXT,
                rating TEXT,
                reviews_count TEXT
            )
            """)

    def process_item(self, item, spider):
        ## Define insert statement
        self.cur.execute("""
                INSERT OR IGNORE INTO movies (rank, title, genres, release_date, age_rating, duration, rating, reviews_count)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
    (
                    item['rank'],
                    item['title'],
                    str(item['genres']),
                    item['release_date'],
                    item['age_rating'],
                    item['duration'],
                    item['rating'],
                    item['reviews_count']
                ))
        self.con.commit()
        self.cur.execute("""
        SELECT * FROM movies ORDER BY rank DESC
        """)
        self.con.commit()
        return item
