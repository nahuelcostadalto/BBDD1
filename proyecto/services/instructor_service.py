from connection import DatabaseConnection
# agregar_instructor es una función que agrega un instructor a la base de datos.
#Creo el ABM de instructor
def agregar_instructor(ci,nombre,apellido):
    query= """INSERT INTO instructores (ci,nombre,apellido) VALUES (%s,%s,%s)""" # %s es un placeholder que se reemplaza por los valores de la tupla values.
    values=(ci,nombre,apellido)
    
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query,values)
            connection.commit()
def eliminar_instructor(ci):
    query="""DELETE FROM instructores WHERE ci=%s"""
    values=(ci,)
    
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query,values)
            connection.commit()

def modificar_instructor(ci,datos_nuevos):
    query = """UPDATE instructores SET nombre=%s, apellido=%s WHERE ci=%s"""
    values = (datos_nuevos["nombre"],datos_nuevos["apellido"],ci)
    
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()

