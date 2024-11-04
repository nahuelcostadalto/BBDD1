from connection import DatabaseConnection

def asignar_clase(ci_instructor, id_actividad, id_turno):
    query = """
        INSERT INTO clase (ci_instructor, id_actividad, id_turno)
        VALUES (%s, %s, %s)
    """
#tengo que valdar que el alumno no esté en la case, hay una funcion de query que lo hace
    values = (ci_instructor, id_actividad, id_turno)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

def agregar_alumno_a_clase(id_clase, ci_alumno, id_equipamiento=None):
    query = """
        INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento)
        VALUES (%s, %s, %s)
    """

    values = (id_clase, ci_alumno, id_equipamiento)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
