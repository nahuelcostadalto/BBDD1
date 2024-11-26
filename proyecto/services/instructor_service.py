from proyecto.connection import DatabaseConnection

# Agregar un instructor a la base de datos
def agregar_instructor(ci, nombre, apellido):
    query = """INSERT INTO instructores (ci, nombre, apellido) VALUES (%s, %s, %s)"""
    values = (ci, nombre, apellido)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cerrar el cursor de forma explícita

def eliminar_instructor(ci):
    query = """DELETE FROM instructores WHERE ci = %s"""
    values = (ci,)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cerrar el cursor de forma explícita

def modificar_instructor(ci, datos_nuevos):
    query = """UPDATE instructores SET nombre = %s, apellido = %s WHERE ci = %s"""
    values = (datos_nuevos["nombre"], datos_nuevos["apellido"], ci)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cerrar el cursor de forma explícita

def obtener_instructores():
    query = """SELECT ci, nombre, apellido FROM instructores"""

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query)
        instructores = cursor.fetchall()  # Recupera todos los resultados de la consulta
        cursor.close()  # Cerrar el cursor de forma explícita

        resultado = [
            {"ci": ci, "nombre": nombre, "apellido": apellido}
            for ci, nombre, apellido in instructores
        ]
    return resultado