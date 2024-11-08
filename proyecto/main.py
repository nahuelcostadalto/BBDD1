#from services.alumnos_service import agregar_alumno
#from services.clase_service import asignar_clase, agregar_alumno_a_clase
#from services.login_service import registrar_usuario, autenticacion_de_usuario
#from datetime import datetime
#from flask import Flask, jsonify, request


# Convertir `fecha_nacimiento` a `datetime.date`
#fecha_nacimiento = datetime.strptime("2000-01-01", "%Y-%m-%d").date()


#try:
    # Usar `fecha_nacimiento` convertido
    #agregar_alumno("12346679", "Juan", "Perez", fecha_nacimiento, "099123456", "jufan@correo.com")

#    print("Alumno agregado correctamente")

#except ValueError as e:
 
 #   print(f"Error: {e}")
from services.alumnos_service import agregar_alumno, eliminar_alumno, modificar_alumno
from services.clase_service import asignar_clase, agregar_alumno_a_clase, quitar_alumno_de_clase, crear_clase, eliminar_clase
from services.instructor_service import agregar_instructor, eliminar_instructor, modificar_instructor
from services.login_service import registrar_usuario, autenticacion_de_usuario
from services.actividades_service import crear_actividad, modificar_actividad, eliminar_actividad
from services.reportes_services import actividad_con_mas_ingresos, actividad_con_mas_alumnos, turno_con_mas_clases

from dominio.Alumno import Alumno
from datetime import datetime

def probar_funcionalidades():
    # Pruebas de Alumno
    print("\n--- Pruebas de Alumno ---")
    alumno = Alumno(ci="50345344", nombre="Nahuel", apellido="Costa", fecha_nacimiento="1998-03-20", telefono="098476546", correo_electronico="nahuel.costa@hotmail.com")
    try:
        agregar_alumno(alumno)
        print("Alumno agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar alumno: {e}")
    
    try:
        modificar_alumno("50345344", {"nombre": "NoSoyNahuel", "apellido": "Inventado", "fecha_nacimiento": "2000-01-01", "telefono": "099654321", "correo_electronico": "Nosoynahuel@hotmail.com"})
        print("Alumno modificado correctamente.")
    except Exception as e:
        print(f"Error al modificar alumno: {e}")
    
#    try:
#        eliminar_alumno("50345344")
#        print("Alumno eliminado correctamente.")
#    except Exception as e:
#        print(f"Error al eliminar alumno: {e}")

    # Pruebas de Actividades
    print("\n--- Pruebas de Actividades ---")
    try:
        crear_actividad("Actividad Random", 500, 15)
        print("Actividad creada correctamente.")
    except Exception as e:
        print(f"Error al crear actividad: {e}")
    
    try:
        modificar_actividad(1, "Actividad Random actualizada", 700, 18)
        print("Actividad modificada correctamente.")
    except Exception as e:
        print(f"Error al modificar actividad: {e}")
    
#    try:
#        eliminar_actividad(1)
#        print("Actividad eliminada correctamente.")
#    except Exception as e:
#        print(f"Error al eliminar actividad: {e}")

    # Pruebas de Clases
    print("\n--- Pruebas de Clases ---")
    try:
        #Crear clase da error Error al crear clase: 1054 (42S22): Unknown column 'es_grupal' in 'field list' chequear en la bbdd si tengo creada esa columna
        crear_clase("50345344", 1, 1, True)
        print("Clase creada correctamente.")
    except Exception as e:
        print(f"Error al crear clase: {e}")
    
    try:
        #asignar clase Error al asignar clase: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`Obligatorio1`.`clase`, CONSTRAINT `clase_ibfk_1` FOREIGN KEY (`ci_instructor`) REFERENCES `instructores` (`ci`) ON DELETE CASCADE)
        asignar_clase("50345344", 1, 1)
        print("Clase asignada correctamente.")
    except Exception as e:
        print(f"Error al asignar clase: {e}")
    #Agregar alumno me está dando el siguiente error Error al agregar alumno a la clase: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`Obligatorio1`.`alumno_clase`, CONSTRAINT `alumno_clase_ibfk_1` FOREIGN KEY (`id_clase`) REFERENCES `clase` (`id`) ON DELETE CASCADE)
    try:
        agregar_alumno_a_clase(1, "50345344")
        print("Alumno agregado a la clase correctamente.")
    except Exception as e:
        print(f"Error al agregar alumno a la clase: {e}")
    
#    try:
#        quitar_alumno_de_clase(1, "50345344")
#        print("Alumno quitado de la clase correctamente.")
#    except Exception as e:
#        print(f"Error al quitar alumno de la clase: {e}")
    
#    try:
#        eliminar_clase(1)
#        print("Clase eliminada correctamente.")
#    except Exception as e:
#        print(f"Error al eliminar clase: {e}")

    # Pruebas de Instructores
    print("\n--- Pruebas de Instructores ---")
    try:
        agregar_instructor("50247454", "Profe", "Random")
        print("Instructor agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar instructor: {e}")
    
    try:
        modificar_instructor("50247454", {"nombre": "ProfeRandom", "apellido": "Modificado"})
        print("Instructor modificado correctamente.")
    except Exception as e:
        print(f"Error al modificar instructor: {e}")
    
#    try:
#        eliminar_instructor("50247454")
#        print("Instructor eliminado correctamente.")
#    except Exception as e:
#        print(f"Error al eliminar instructor: {e}")

    # Pruebas de Usuarios
    print("\n--- Pruebas de Usuarios ---")
    try:
        registrar_usuario("pruebaregistro@correo.com", "password123")
        print("Usuario registrado correctamente.")
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
    
    try:
        autenticado = autenticacion_de_usuario("pruebaregistro@correo.com", "password123")
        if autenticado:
            print("Usuario autenticado correctamente.")
        else:
            print("Error en la autenticación de usuario.")
    except Exception as e:
        print(f"Error al autenticar usuario: {e}")


if __name__ == "__main__":
    probar_funcionalidades()
