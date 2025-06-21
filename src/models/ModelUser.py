from dataclasses import dataclasss
from .entities.user import User

@dataclasss
class ModelUser:
    
    
    @classmethod
    def login(cls,db,user):
        try:
            db.connect() 
            cursor = db.get_cursor()
            query = "SELECT no_control, contra FROM usuarios WHERE no_control = %s"
            cursor.execute(query,(user.no_control)) 
            row = cursor.fetchone()
            if row != None:
                user = User(row[0],User.check_password(row[1],User.password))
                return user
        except Exception as e:
            print(f"Error in ModelUser.login: {e}")
            return False
        
    