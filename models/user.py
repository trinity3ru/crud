

class User:
    def  __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def greet(self):
        return "Привет я пользователь, мой ник {self.username}"    
    def ret(self):
        return  f"{self.username} | {self.password}  | {self.email}"