from connection import DatabaseConnection
from dominio import Alumno
from utils.validators import validar_email

#Tenemos Agregar Alumno, el cual agrega un alumno a la tabla alumnos de la base de datos.
#Tenemos Eliminar Alumno, el cual elimina un alumno de la tabla alumnos de la base de datos.
#Tenemos modificar Alumno, el cual modifica los datos de un alumno en la tabla alumnos de la base de datos.
#Es decir ya tenemos el ABM de alumnos completo.
def agregar_alumno(alumno):

    print("aca llegue1")
#explota acá adentro
   # alumno = Alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico)

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

    print("llegue a la bd :D:D")  # Debug    
    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()

def eliminar_alumno(ci):
    query = """DELETE FROM alumnos WHERE ci=%s"""
    values = (ci,)

    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()

def modificar_alumno(ci,datos_nuevos):
    query = """UPDATE alumnos SET nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono=%s, correo_electronico=%s WHERE ci=%s"""
    values = (datos_nuevos["nombre"],datos_nuevos["apellido"],datos_nuevos["fecha_nacimiento"],datos_nuevos["telefono"],datos_nuevos["correo_electronico"],ci)

    with DatabaseConnection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()