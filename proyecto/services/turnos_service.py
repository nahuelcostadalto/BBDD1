import datetime
from proyecto.connection import DatabaseConnection
#Turnos es autoincremental con el ID en la bbdd, tenemos que cambiarlo , porque sino cada vez que lo vamos a cambiar tenemos que hacerlo manualmente , porque no sabemos
#a que id corresponde cada turno.
def crear_turno(hora_inicio,hora_fin):
    query = """INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)"""
    values = (hora_inicio, hora_fin)
    
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
def eliminar_turno(id_turno):
    query = """DELETE FROM turnos WHERE id_turno=%s"""
    values = (id_turno,)
    
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
#MODIFCAR LA TABLA TURNOS PARA QUE EL ID SE LLAME id_turnos.
def modificar_turno(id_turno, hora_inicio, hora_fin):
    query = """UPDATE turnos SET hora_inicio=%s, hora_fin=%s WHERE id=%s"""
    values = (hora_inicio, hora_fin, id_turno)  # Cambiado el orden y cantidad de parámetros

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
