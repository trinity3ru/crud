from .user import User

class Bot:
    def __init__(self, owner:int, token:str, git_http:str):
        self._owner = owner
        self._token = token
        self._gitHttp = git_http



    def get_ownerID(self) ->int:
        return self._owner.get_id()

    def get_token(self)->str:
        return self._token


    def get_git(self)->str:
        return self._gitHttp

