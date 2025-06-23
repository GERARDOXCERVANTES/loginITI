from dataclasses import dataclass
from .entities.user import User

@dataclass
class ModelUser:

    @classmethod
    def login(cls,db,user):
        try:
            db.connect() 
            cursor = db.get_cursor()
            query = "SELECT no_control, contra FROM usuarios WHERE no_control = %s"
            cursor.execute(query,(user.no_control,)) 
            row = cursor.fetchone()
            if row != None:
                authenticated_user = User(row[0], User.check_password(row[1], user.password))
                return authenticated_user
        except Exception as e:
            print(f"Error in ModelUser.login: {e}")
            return False
        finally:
            db.close_all()
        
    @classmethod
    def by_id(cls, db, get_id):
        try:
            db.connect() 
            cursor = db.get_cursor()
            query = "SELECT no_control, contra FROM usuarios WHERE no_control = %s"
            cursor.execute(query, (get_id,))
            row = cursor.fetchone()
            if row != None:
                return User(row[0],None)
            else:
                return None
        except Exception as e:
            print(f"Error in ModelUser.by_id: {e}")
            return None
        finally:
            db.close_all()