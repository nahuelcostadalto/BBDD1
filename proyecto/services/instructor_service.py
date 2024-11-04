from connection import DatabaseConnection

def agregar_instructor(ci,nombre,apellido):
    query= """INSERT INTO instructor (ci,nombre,apellido) VALUES (%s,%s,%s)"""
    values=(ci,nombre,apellido)
    
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query,values)
            connection.commit()