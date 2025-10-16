import sqlite3

from models.user import User 
from models.bot import Bot


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
                INSERT OR IGNORE INTO users (username, login, password, email) VALUES (?, ?, ?, ?)
                """, (user.username, user.login, user.password, user.email)
            )
        except sqlite3.InternalError as e:
            print(f"Error: {e}")
            conn.close()
            return None  
        conn.commit()
        user_id = sql.lastrowid
        print(f"User added {user_id}") 
        
        conn.close()
        return user_id 

    def get_all_users(self):
        conn = sqlite3.connect(self.db_host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    def add_bot(self, bot:Bot)->None:
        conn = sqlite3.connect(self.db_host)
        sql = conn.cursor()
        try:
            sql.execute(
                """
                INSERT INTO bots (token, git, user_id) VALUES (?, ?, ?)
                """, (bot.get_token(), bot.get_git(), bot.get_user_id())
            )
        except sqlite3.InternalError as e:
            print(f"Error: {e}")
            conn.close()
            return None  
        conn.commit()
        bot_id = sql.lastrowid
        print(f"Bot added {bot_id}") 
        conn.close()
        return bot_id
          
        


 