from connection import DatabaseConnection
# Creo el ABM de actividades (fijarme en la letra si era obligatorio este ABM)

def crear_actividad(descripcion, costo, edad_minima):
    query = "INSERT INTO actividades (descripcion, costo, edad_minima) VALUES (%s, %s, %s)"
    values = (descripcion, costo, edad_minima)
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()


def modificar_actividad(id, nueva_descripcion, nuevo_costo, nueva_edad_minima):
    query = "UPDATE actividades SET descripcion = %s, costo = %s, edad_minima = %s WHERE id = %s"
    values = (nueva_descripcion, nuevo_costo, nueva_edad_minima, id)
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()

def eliminar_actividad(id):
    query = "DELETE FROM actividades WHERE id = %s"
    values = (id,)
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
    