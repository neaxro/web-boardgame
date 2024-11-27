import mysql.connector

from config import Config


class BoardgameDB:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(BoardgameDB, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        config = Config()

        self.db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            db=config.DB_DATABASE
        )

    def get_all(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM boardgame")

        return cursor.fetchall()

    def get_id(self, id: int):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM boardgame WHERE id = %s", (id,))
        
        return cursor.fetchall()
    
    def get_title(self, title: str):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM boardgame WHERE LOWER(title) LIKE %s", (f"%{title.lower()}%",))
        
        return cursor.fetchall()

    def insert(self, boardgame_data: dict):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO boardgame
            (title, category, description, tags, min_players, max_players, best_players, min_age, avg_time, played_count) VALUES
            (%(title)s, %(category)s, %(description)s, %(tags)s, %(min_players)s, %(max_players)s, %(best_players)s, %(min_age)s, %(avg_time)s, 0)
            """,
            (boardgame_data)
        )

        return cursor.lastrowid
    
    def update(self, boardgame_data: dict):
        cursor = self.db.cursor()
        cursor.execute(
            """
            UPDATE boardgame
            SET title=%(title)s, category=%(category)s, description=%(description)s,
            tags=%(tags)s, min_players=%(min_players)s, max_players=%(max_players)s,
            best_players=%(best_players)s, min_age=%(min_age)s, avg_time=%(avg_time)s,
            played_count=%(played_count)s
            WHERE id = %(id)s
            """,
            (boardgame_data)
        )
        return cursor.rowcount

    def delete(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM boardgame WHERE id = %s", (id, ))
        return cursor.rowcount
