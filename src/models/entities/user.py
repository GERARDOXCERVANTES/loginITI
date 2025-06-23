from dataclasses import dataclass
from werkzeug.security import check_password_hash
from flask_login import UserMixin
@dataclass
class User(UserMixin):
    no_control: str
    password: str
    
    def get_id(self):
        return self.no_control  # de usermixin es requerido para indentificar al usuario
    
    @staticmethod
    def check_password(hash_password,password):
        return check_password_hash(hash_password,password)
