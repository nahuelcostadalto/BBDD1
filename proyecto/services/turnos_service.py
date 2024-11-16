
from datetime import datetime
from proyecto.connection import DatabaseConnection
#Turnos es autoincremental con el ID en la bbdd, tenemos que cambiarlo , porque sino cada vez que lo vamos a cambiar tenemos que hacerlo manualmente , porque no sabemos
#a que id corresponde cada turno.
def crear_turno(hora_inicio, hora_fin):
    # Convertir strings de hora a objetos de tiempo si es necesario
    if isinstance(hora_inicio, str):
        hora_inicio = datetime.strptime(hora_inicio, "%H:%M").time()
    if isinstance(hora_fin, str):
        hora_fin = datetime.strptime(hora_fin, "%H:%M").time()

    query = """INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)"""
    values = (hora_inicio, hora_fin)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
def eliminar_turno(id):
    query = """DELETE FROM turnos WHERE id=%s"""
    values = (id,)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

def modificar_turno(id, hora_inicio, hora_fin):
    # Convertir strings de hora a objetos de tiempo si es necesario
    if isinstance(hora_inicio, str):
        hora_inicio = datetime.strptime(hora_inicio, "%H:%M").time()
    if isinstance(hora_fin, str):
        hora_fin = datetime.strptime(hora_fin, "%H:%M").time()

    query = """UPDATE turnos SET hora_inicio=%s, hora_fin=%s WHERE id=%s"""
    values = (hora_inicio, hora_fin, id)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
from datetime import time

def obtener_todos_los_turnos():
    query = """SELECT id, hora_inicio, hora_fin FROM turnos"""

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        turnos = cursor.fetchall()  # Recupera todos los resultados de la consulta

        resultado = [
            {
                "id": id,
                "hora_inicio": hora_inicio.strftime("%H:%M") if isinstance(hora_inicio, time) else str(hora_inicio),
                "hora_fin": hora_fin.strftime("%H:%M") if isinstance(hora_fin, time) else str(hora_fin)
            }
            for id, hora_inicio, hora_fin in turnos
        ]
        return resultado