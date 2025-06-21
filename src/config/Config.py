import psycopg2 as datab
from dataclasses import dataclass
from typing import Dict


@dataclass
class DatabaseConnection:
    
    config: Dict[str, any]
    connection = None
    
    
    
    def connect(self):
        try:
            if self.connection and not self.connection.closed:
                print("ya existe coneccion a esta base")
                return True
            
            self.connection = datab.connect(
                dbname= self.config["dbname"],
                user= self.config["user"],
                password= self.config["password"],
                host= self.config["host"],
                port= self.config["port"]
            )
            print("CONNECION EXITOSA")
            return True
        except Exception as e:
            print(f"ERROR A CONECTAR ALA DATABASE: {e}")
            return False   
        
        
        
    def close_all(self):
        try:
            if self.connection and not self.connection.closed:
                self.connection.close()
                
            print("CERRAR LA BASE DE DATOS")
   
        except Exception as e:
            print(F"ERROR AL CERRAR LA BASE DE DATOS {e}")
            
    def get_cursor(self):
        try:
            return self.connection.cursor()
        except Exception as e:
            print(f"ERROR AL OBTENER EL CURSOR: {e}")
            return None
        
    def get_commit(self):
        try:
            return self.connection.commit()
        except Exception as e:
            print(f"ERROR AL HACER COMMIT: {e}")
            return None
        
        
def Conn():
    return {
        'dbname' :"login-test",
        'user' :"postgres",
        'password' :"arbolmedico",
        'host' :"localhost",
        'port' :5432
        }
    
