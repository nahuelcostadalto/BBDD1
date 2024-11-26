from proyecto.connection import DatabaseConnection

# Crear un nuevo equipamiento en la base de datos
def crear_equipamiento(nombre, descripcion, costo):
    query = """INSERT INTO equipamiento (nombre, descripcion, costo) VALUES (%s, %s, %s)"""
    values = (nombre, descripcion, costo)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cerrar el cursor de forma explícita

# Eliminar un equipamiento por ID
def eliminar_equipamiento(id_equipamiento):
    query = """DELETE FROM equipamiento WHERE id = %s"""
    values = (id_equipamiento,)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cerrar el cursor de forma explícita

# Modificar los datos de un equipamiento existente
def modificar_equipamiento(id_equipamiento, nombre, descripcion, costo):
    query = """UPDATE equipamiento SET nombre = %s, descripcion = %s, costo = %s WHERE id = %s"""
    values = (nombre, descripcion, costo, id_equipamiento)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cerrar el cursor de forma explícita

# Obtener todos los equipamientos registrados en la base de datos
def obtener_equipamientos():
    query = """SELECT id, nombre, descripcion, costo FROM equipamiento"""

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query)
        equipamientos = cursor.fetchall()  # Recuperar todos los resultados de la consulta
        cursor.close()  # Cerrar el cursor de forma explícita

        # Convertir los resultados en una lista de diccionarios
        resultado = [
            {"id": id, "nombre": nombre, "descripcion": descripcion, "costo": costo}
            for id, nombre, descripcion, costo in equipamientos
        ]
    return resultado