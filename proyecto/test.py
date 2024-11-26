from services.alumnos_service import agregar_alumno, eliminar_alumno, modificar_alumno
from services.clase_service import asignar_clase, agregar_alumno_a_clase, quitar_alumno_de_clase, crear_clase, eliminar_clase
from services.instructor_service import agregar_instructor, eliminar_instructor, modificar_instructor
from services.login_service import registrar_usuario, autenticacion_de_usuario
from services.actividades_service import crear_actividad, modificar_actividad, eliminar_actividad
from services.turnos_service import crear_turno, modificar_turno, eliminar_turno
from dominio.Alumno import Alumno
from services.reportes_services import actividad_con_mas_ingresos, actividad_con_mas_alumnos, turno_con_mas_clases
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

    try:
        eliminar_alumno("50345344")
        print("Alumno eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar alumno: {e}")

    # Pruebas de Actividades
    print("\n--- Pruebas de Actividades ---")
    try:
        crear_actividad("Actividad de prueba con más alumnos", 500, 15)
        print("Actividad creada correctamente.")
    except Exception as e:
        print(f"Error al crear actividad: {e}")

    try:
        modificar_actividad(1, "Actividad Random actualizada", 700, 18)
        print("Actividad modificada correctamente.")
    except Exception as e:
        print(f"Error al modificar actividad: {e}")

    try:
        eliminar_actividad(1)
        print("Actividad eliminada correctamente.")
    except Exception as e:
        print(f"Error al eliminar actividad: {e}")

    # Pruebas de Clases
    print("\n--- Pruebas de Clases ---")
    try:
        crear_clase("12345678", 23, 1)
        print("Clase creada correctamente.")
    except Exception as e:
        print(f"Error al crear clase: {e}")

    try:
        asignar_clase("50247454", 2, 1)
        print("Clase asignada correctamente.")
    except Exception as e:
        print(f"Error al asignar clase: {e}")

    try:
        agregar_alumno_a_clase(42, "12346679")
        agregar_alumno_a_clase(42, "12347448")
        agregar_alumno_a_clase(42, "12387448")
        agregar_alumno_a_clase(42, "50345344")
        agregar_alumno_a_clase(42, "12345678")
        print("Alumno agregado a la clase correctamente.")
    except Exception as e:
        print(f"Error al agregar alumno a la clase: {e}")

    try:
        quitar_alumno_de_clase(1, "50345344")
        print("Alumno quitado de la clase correctamente.")
    except Exception as e:
        print(f"Error al quitar alumno de la clase: {e}")

    try:
        eliminar_clase(1)
        print("Clase eliminada correctamente.")
    except Exception as e:
        print(f"Error al eliminar clase: {e}")

    # Pruebas de Instructores
    print("\n--- Pruebas de Instructores ---")
    try:
        agregar_instructor("12345678", "Profe", "prueba con más alumnos")
        print("Instructor agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar instructor: {e}")

    try:
        modificar_instructor("50247454", {"nombre": "ProfeRandom", "apellido": "Modificado"})
        print("Instructor modificado correctamente.")
    except Exception as e:
        print(f"Error al modificar instructor: {e}")

    try:
        eliminar_instructor("50247454")
        print("Instructor eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar instructor: {e}")

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

    print("\n--- Pruebas de Reportes ---")
    try:
        actividad = actividad_con_mas_ingresos()
        print(f"Actividad con más ingresos: {actividad}")
    except Exception as e:
        print(f"Error al obtener actividad con más ingresos: {e}")

    try:
        actividad = actividad_con_mas_alumnos()
        print(f"Actividad con más alumnos: {actividad}")
    except Exception as e:
        print(f"Error al obtener actividad con más alumnos: {e}")

    def convertir_timedelta_a_hora(timedelta_obj):
        horas = timedelta_obj.seconds // 3600
        minutos = (timedelta_obj.seconds // 60) % 60
        return f"{horas:02d}:{minutos:02d}"

    print("\n--- Pruebas de Reportes ---")
    try:
        turno = turno_con_mas_clases()
        if turno:
            hora_inicio, hora_fin, total_clases = turno
            hora_inicio_str = convertir_timedelta_a_hora(hora_inicio)
            hora_fin_str = convertir_timedelta_a_hora(hora_fin)
            print(f"Turno con más clases: Inicio {hora_inicio_str}, Fin {hora_fin_str}, Total de clases: {total_clases}")
        else:
            print("No se encontró ningún turno con clases.")
    except Exception as e:
        print(f"Error al obtener turno con más clases: {e}")

if __name__ == "__main__":
    probar_funcionalidades()