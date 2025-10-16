

class User:
    def  __init__(self, login: str, password:str, email: str, id: int|None = None, username: str|None = None):
        self.username = username
        self.password = password
        self.email = email
        self.login = login
        self.id = id

    def get_id(self)-> int|None:
        return self.id

    def greet(self):
        if self.username:
            return f"Привет я пользователь, мой ник {self.username}"   
        else:
            return f"Привет я пользователь, мой ник {self.login}"    
        
    def ret(self):
        return  f"{self.username or self.login}| {self.password}  | {self.email}|{self.id}"