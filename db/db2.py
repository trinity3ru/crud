import sqlite3

from models.user import User 


class DBManager:
    def __init__(self):
        self.db_host = "sqlite.db"
        self.create_tables()

    def create_tables(self):
        db = sqlite3.connect(self.db_host)
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(15) UNIQUE, username VARCHAR(15), password VARCHAR(15), email VARCHAR(25))
            """
        )
        cursor.execute("""CREATE TABLE IF NOT EXISTS bots (id INTEGER PRIMARY KEY AUTOINCREMENT, token VARCHAR(30), git VARCHAR(100), user_id INTEGER);  """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, action VARCHAR(150), time DATATIME DEFAULT NOW(), user_id INTEGER);  """)
        db.commit()
        db.close()


    def add_user (self, user:User):
        conn = sqlite3.connect(self.db_host)
        sql = conn.cursor()
        try:
            sql.execute(
                """
                INSERT OR IGNORE INTO users (username, password, email) VALUES (?, ?, ?)
                """, (user.username, user.password, user.email)
            )
        except sqlite3.InternalError as e:
            print(f"Error: {e}")
            conn.close()
            return None  
        conn.commit()
        conn.close()  
        return sql.fetchone()
    
    def add_bot(self, bot:Bot)->None:
        conn = sqlite3.connect(self.db_host)
        sql = conn.cursor()
        try:
            sql.execute(
                """
                INSERT INTO bots (token, git, userid) VALUES (?, ?, ?)
                """, (bot.get_token(), bot.get_git(), bot.get_ownerID() )
            )
        except sqlite3.InternalError as e:
            print(f"Error: {e}")
            conn.close()
            return None  
        conn.commit()
        conn.close()  
        return sql.fetchone()


 