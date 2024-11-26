from datetime import datetime, time
from proyecto.connection import DatabaseConnection

# Función para validar y convertir horas
def convertir_hora(hora):
    """
    Convierte una hora en formato HH:MM:SS o HH:MM a un objeto time.
    Lanza un ValueError si el formato no es válido.
    """
    formatos = ["%H:%M:%S", "%H:%M"]  # Permitir ambos formatos
    for formato in formatos:
        try:
            return datetime.strptime(hora, formato).time()
        except ValueError:
            continue  # Intentar con el siguiente formato
    raise ValueError(f"Formato de hora no válido: {hora}. Debe ser HH:MM:SS o HH:MM.")

# Crear turno
def crear_turno(hora_inicio, hora_fin):
    # Validar y convertir las horas
    hora_inicio = convertir_hora(hora_inicio)
    hora_fin = convertir_hora(hora_fin)

    query = """INSERT INTO turnos (hora_inicio, hora_fin) VALUES (%s, %s)"""
    values = (hora_inicio, hora_fin)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

# Eliminar turno
def eliminar_turno(id):
    query = """DELETE FROM turnos WHERE id=%s"""
    values = (id,)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

# Modificar turno
def modificar_turno(id, hora_inicio, hora_fin):
    # Validar y convertir las horas
    hora_inicio = convertir_hora(hora_inicio)
    hora_fin = convertir_hora(hora_fin)

    query = """UPDATE turnos SET hora_inicio=%s, hora_fin=%s WHERE id=%s"""
    values = (hora_inicio, hora_fin, id)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

# Obtener todos los turnos
def obtener_todos_los_turnos():
    query = """SELECT id, hora_inicio, hora_fin FROM turnos"""

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        turnos = cursor.fetchall()  # Recupera todos los resultados de la consulta

        resultado = [
            {
                "id": id,
                # Formatear las horas con segundos
                "hora_inicio": hora_inicio.strftime("%H:%M:%S") if isinstance(hora_inicio, time) else str(hora_inicio),
                "hora_fin": hora_fin.strftime("%H:%M:%S") if isinstance(hora_fin, time) else str(hora_fin)
            }
            for id, hora_inicio, hora_fin in turnos
        ]
        return resultado