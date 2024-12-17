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
        cursor = None
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM boardgame")

            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()

    def get_id(self, id: int):
        cursor = None
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM boardgame WHERE id = %s", (id,))
            
            return cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()
    
    def get_title(self, title: str):
        cursor = None
        try:
            cursor = self.db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM boardgame WHERE LOWER(title) LIKE %s", (f"%{title.lower()}%",))
            
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()

    def insert(self, boardgame_data: dict):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO boardgame
                (title, category, description, tags, min_players, max_players, best_players, min_age, avg_time, played_count) VALUES
                (%(title)s, %(category)s, %(description)s, %(tags)s, %(min_players)s, %(max_players)s, %(best_players)s, %(min_age)s, %(avg_time)s, 0)
                """,
                boardgame_data
            )
            
            self.db.commit()
            return cursor.lastrowid
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            cursor.close()
    
    def update(self, boardgame_data: dict):
        cursor = self.db.cursor()
        try:
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
            
            self.db.commit()
            return cursor.rowcount
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            cursor.close()

    def delete(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM boardgame WHERE id = %s", (id, ))
            self.db.commit()
            return cursor.rowcount
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            cursor.close()
