from db.db2 import DBManager
from models.user import User
from random import randint, choice

# name_arr = ['Danil', 'nataly', 'Petr']

# def main():
#     db = DBManager()
#     print('-'*60)

#     for i in range(100):
#         name = choice(name_arr) 
#         user = User(name, randint(100000, 999999 ), f"{name}{randint(432, 768)}@testmail.com")
#         db.add_user(user)
#         print(f"User #{i} created {user.ret()}" )


# # if __name__ == __main__:
# main()


"""Пакет взаимодействия с БД"""
from .db2 import DBManager

from random import randint, choice

def main() ->None:
  db= DBManager()
  login_arr = ['qwerty','admin1','logn2', 'simple_user']
  for i in range(100):
     print(f"#{i}" end=f"{' ' * (5 - len(str(i))}")
     login = choice(login_arr) + str(i)
     user = User(login, randint(10000000, 9999999), f"{login}{randint(100,999)}@test.com" )
     db.add_user(user)
     for j in range(3): 
        bot = Bot(user, "token", "http")
        db.add_bot(bot)
        print(f"bot {j} - создан")
                
                 
                 
     
     




if __name__== '__main__':
    main()