from proyecto.connection import DatabaseConnection
#Tenemos el ABM de clases completo.
#asignar_clase, el cual asigna un instructor a una clase.
#agregar_alumno_a_clase, el cual agrega un alumno a una clase.
#quitar_alumno_de_clase el cual quita un alumno de la clase
#crear_clase Creamos una nueva clase y le asignamos un instructor(por CI) ,actividad(por ID),turno_id(por id),y si es grupal o no es_grupal
def asignar_clase(ci_instructor, id_actividad, id_turno): #asignar a una clase un instructor
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

def quitar_alumno_de_clase(id_clase, ci_alumno):
    query = """
        DELETE FROM alumno_clase
        WHERE id_clase=%s AND ci_alumno=%s
    """

    values = (id_clase, ci_alumno)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
##si nos importa si es grupal agregamos el atributo es_grupal , lo pasamos e la query, lo agregamos a valores y a values
def crear_clase(ci_instructor,actividad_id,turno_id):
    query = """
        INSERT INTO clase (ci_instructor, id_actividad, id_turno)
        VALUES (%s, %s, %s)
    """
    values = (ci_instructor,actividad_id,turno_id)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

def eliminar_clase(id_clase):
    query = """DELETE FROM clase WHERE id_clase=%s"""
    values = (id_clase,)

    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

#falta crear el eliminar instructor de la clase.
def quitar_instructor_de_clase(id_clase, ci_instructor):
    query = """
        DELETE FROM clase
        WHERE id_clase=%s AND ci_instructor=%s
    """

    values = (id_clase, ci_instructor)

#Falta el cambiar instructor de clase (Lo vamos a hacer tipo swap o agregamos y quitamos con las funcionalidades actuales? )