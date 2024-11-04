from connection import DatabaseConnection
from dominio import Alumno
from utils.validators import validar_email

def agregar_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico):

    print("aca llegue1")

    alumno = Alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico)

    print("aca llegue2")

    # Validar correo electrónico
    if not validar_email(alumno.correo_electronico):
        raise ValueError("Correo electrónico inválido")
    
    print("aca llegu2e4")

    if not alumno.es_mayor_de_edad():
        raise ValueError("El alumno debe ser mayor de edad")

    print("aca llegue3")

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

    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
