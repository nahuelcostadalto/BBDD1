from datetime import timedelta

from proyecto.connection import DatabaseConnection

def convertir_timedelta_a_hh_mm(value):
    """Convierte un objeto timedelta a una cadena HH:MM."""
    if isinstance(value, timedelta):
        total_seconds = value.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}"
    return value  # Devuelve el valor original si no es timedelta

def actividad_con_mas_ingresos():
    query = """
        SELECT a.descripcion AS actividad, 
               SUM(a.costo + IFNULL(e.costo, 0)) AS ingresos
        FROM actividades a
        JOIN clase c ON a.id = c.id_actividad
        JOIN alumno_clase ac ON c.id = ac.id_clase
        LEFT JOIN equipamiento e ON ac.id_equipamiento = e.id
        GROUP BY a.descripcion
        ORDER BY ingresos DESC
        LIMIT 1
    """
    with DatabaseConnection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchone()

def actividad_con_mas_alumnos():
    query = """
        SELECT a.descripcion, COUNT(ac.ci_alumno) AS total_alumnos
        FROM actividades a
        JOIN clase c ON a.id = c.id_actividad
        JOIN alumno_clase ac ON c.id = ac.id_clase
        GROUP BY a.descripcion
        ORDER BY total_alumnos DESC
        LIMIT 1
    """
    try:
        with DatabaseConnection() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
    except Exception as e:
        raise e

def turno_con_mas_clases():
    query = """
        SELECT t.hora_inicio, 
               t.hora_fin, 
               COUNT(c.id) AS total_clases,
               CONCAT(i.nombre, ' ', i.apellido) AS docente
        FROM turnos t
        JOIN clase c ON t.id = c.id_turno
        JOIN instructores i ON c.ci_instructor = i.ci
        GROUP BY t.hora_inicio, t.hora_fin, i.nombre, i.apellido
        ORDER BY total_clases DESC
        LIMIT 1
    """
    with DatabaseConnection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchone()
        # Convertir timedelta a HH:MM si aplica
        if result:
            result["hora_inicio"] = convertir_timedelta_a_hh_mm(result["hora_inicio"])
            result["hora_fin"] = convertir_timedelta_a_hh_mm(result["hora_fin"])
        return result