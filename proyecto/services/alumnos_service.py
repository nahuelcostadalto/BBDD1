from proyecto.connection import DatabaseConnection
from proyecto.dominio import Alumno
from proyecto.utils.validators import validar_email

#Tenemos Agregar Alumno, el cual agrega un alumno a la tabla alumnos de la base de datos.
#Tenemos Eliminar Alumno, el cual elimina un alumno de la tabla alumnos de la base de datos.
#Tenemos modificar Alumno, el cual modifica los datos de un alumno en la tabla alumnos de la base de datos.
#Es decir ya tenemos el ABM de alumnos completo.
def agregar_alumno(alumno):
    # Validar correo electrónico
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
        alumno.correo_electronico
    )

    connection = DatabaseConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def eliminar_alumno(ci):
    query = """DELETE FROM alumnos WHERE ci=%s"""
    values = (ci,)

    connection = DatabaseConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    finally:
        cursor.close()
        connection.close()


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
        ci
    )

    connection = DatabaseConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def obtener_todos_los_alumnos():
    query = """SELECT ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico FROM alumnos"""

    connection = DatabaseConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        alumnos = cursor.fetchall()

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
    finally:
        cursor.close()
        connection.close()