from dataclasses import dataclass
from werkzeug.security import check_password_hash

@dataclass
class User:
    no_control: str
    password: str
    
    @classmethod
    def check_password(self,hash_password,password):
        return check_password_hash(hash_password,password)
