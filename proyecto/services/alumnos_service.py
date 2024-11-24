from proyecto.connection import DatabaseConnection
from proyecto.dominio import Alumno
from proyecto.utils.validators import validar_email

def agregar_alumno(alumno):
    if not validar_email(alumno.correo_electronico):
        raise ValueError("Correo electrónico inválido")
    if not alumno.es_mayor_de_edad():
        raise ValueError("El alumno debe ser mayor de edad")

    query = """
        INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        alumno.ci,
        alumno.nombre,
        alumno.apellido,
        alumno.fecha_nacimiento,
        alumno.telefono,
        alumno.correo_electronico,
    )

    try:
        with DatabaseConnection() as connection:
            cursor = connection.cursor()  # Crea el cursor manualmente
            cursor.execute(query, values)
            connection.commit()
            cursor.close()  # Cierra el cursor manualmente
    except Exception as e:
        print(f"Error en agregar_alumno: {e}")
        raise


def eliminar_alumno(ci):
    query = """DELETE FROM alumnos WHERE ci=%s"""
    values = (ci,)

    try:
        with DatabaseConnection() as connection:
            cursor = connection.cursor()  # Crea el cursor manualmente
            cursor.execute(query, values)
            connection.commit()
            cursor.close()  # Cierra el cursor manualmente
    except Exception as e:
        print(f"Error en eliminar_alumno: {e}")
        raise


def modificar_alumno(ci, datos_nuevos):
    query = """
        UPDATE alumnos 
        SET nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono=%s, correo_electronico=%s 
        WHERE ci=%s
    """
    values = (
        datos_nuevos["nombre"],
        datos_nuevos["apellido"],
        datos_nuevos["fecha_nacimiento"],
        datos_nuevos["telefono"],
        datos_nuevos["correo_electronico"],
        ci,
    )

    try:
        with DatabaseConnection() as connection:
            cursor = connection.cursor()  # Crea el cursor manualmente
            cursor.execute(query, values)
            connection.commit()
            cursor.close()  # Cierra el cursor manualmente
    except Exception as e:
        print(f"Error en modificar_alumno: {e}")
        raise


def obtener_todos_los_alumnos():
    query = """SELECT ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico FROM alumnos"""

    try:
        with DatabaseConnection() as connection:
            cursor = connection.cursor()  # Crea el cursor manualmente
            cursor.execute(query)
            alumnos = cursor.fetchall()
            cursor.close()  # Cierra el cursor manualmente
    except Exception as e:
        print(f"Error en obtener_todos_los_alumnos: {e}")
        raise

    resultado = [
        {
            "ci": ci,
            "nombre": nombre,
            "apellido": apellido,
            "fecha_nacimiento": fecha_nacimiento,
            "telefono": telefono,
            "correo_electronico": correo_electronico,
        }
        for ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico in alumnos
    ]
    return resultado