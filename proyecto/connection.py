import os
import mysql.connector
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()


class DatabaseConnection:
    def __init__(self):
        self.config = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'),
            'port': os.getenv('DB_PORT')
        }
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        print("Conexión exitosa a la base de datos")
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")


"""import os
import mysql.connector
#Nos encargamos de establecer la conexión con la base de datos, para ello utilizamos la libreria myql.connector la cual utilizamos en el practico 2

config = {
    'user': 'root', #Dejamos el usuario que nos da el profesor en los practicos 1 
    'password': 'rootpassword', #contraseña dada por el profesor
    'host': 'localhost',
    'database': 'Obligatorio1',  # Reemplaza con el nombre de tu base de datos
    'port': 3306,  # El puerto por defecto de MySQL
    'raise_on_warnings': True
}

# Inicializar la variable de conexión
connection = None

try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Verificar si la conexión no es None y si está conectada antes de cerrarla
    if connection is not None and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
"""
