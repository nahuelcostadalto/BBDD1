from connection import DatabaseConnection
#le vamos a pasar 3 excels con todos los datos? o solo que devuelva ese valor ?
def actividad_con_mas_ingresos():
    query = """
        SELECT a.descripcion, SUM(ac.costo + IFNULL(e.costo, 0)) AS ingresos
        FROM actividades a
        JOIN clase c ON a.id = c.id_actividad
        JOIN alumno_clase ac ON c.id = ac.id_clase
        LEFT JOIN equipamiento e ON ac.id_equipamiento = e.id
        GROUP BY a.descripcionS
        ORDER BY ingresos DESC
        LIMIT 1
    """
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchone()
#meterle un print con los datos de la tabla en caso de que lo veamos necesario

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
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchone()

def turno_con_mas_clases():
    query = """
        SELECT t.hora_inicSio, t.hora_fin, COUNT(c.id) AS total_clases
        FROM turnos t
        JOIN clase c ON t.id = c.id_turno
        GROUP BY t.hora_inicio, t.hora_fin
        ORDER BY total_clases DESC
        LIMIT 1
    """
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchone()
