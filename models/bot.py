 

class Bot:
    def __init__(self, user_id:int, token:str, git_http:str):
        self.user_id = user_id
        self.token = token
        self.git_http = git_http



    def get_owner_id(self) ->int:
        return self.user_id

    def get_token(self)->str:
        return self.token


    def get_git(self)->str:
        return self.git_http
    

    def __repr__(self):
        return  f" <Вот user_id {self.user_id}, token=' {self.token[:5]}...', git=' {self.git_http}'>"


