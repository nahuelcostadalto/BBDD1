from proyecto.connection import DatabaseConnection


# Función para modificar una actividad
def modificar_actividad(id, nueva_descripcion, nuevo_costo, nueva_edad_minima):
    query = "UPDATE actividades SET descripcion = %s, costo = %s, edad_minima = %s WHERE id = %s"
    values = (nueva_descripcion, nuevo_costo, nueva_edad_minima, id)
    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crea el cursor explícitamente
        cursor.execute(query, values)
        connection.commit()
        cursor.close()  # Cierra el cursor manualmente

def obtener_actividades():
    query = "SELECT id, descripcion, costo, edad_minima FROM actividades"

    with DatabaseConnection() as connection:
        cursor = connection.cursor()  # Crear el cursor explícitamente
        cursor.execute(query)
        actividades = cursor.fetchall()  # Recupera todos los resultados de la consulta
        cursor.close()  # Cerrar el cursor de forma explícita

        resultado = [
            {"id": id, "descripcion": descripcion, "costo": costo, "edad_minima": edad_minima}
            for id, descripcion, costo, edad_minima in actividades
        ]
    return resultado