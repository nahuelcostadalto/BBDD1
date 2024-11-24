from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

# Importación de servicios
from services.alumnos_service import agregar_alumno, eliminar_alumno, modificar_alumno, obtener_todos_los_alumnos
from services.clase_service import asignar_clase, agregar_alumno_a_clase, quitar_alumno_de_clase, eliminar_clase, obtener_clases,actualizar_dictada, crear_clase
from services.login_service import registrar_usuario, autenticacion_de_usuario
from services.actividades_service import modificar_actividad, obtener_actividades
from services.instructor_service import agregar_instructor, eliminar_instructor, modificar_instructor, obtener_instructores
from services.reportes_services import actividad_con_mas_ingresos, actividad_con_mas_alumnos, turno_con_mas_clases
from services.turnos_service import crear_turno, modificar_turno, eliminar_turno, obtener_todos_los_turnos
from dominio.Alumno import Alumno

# Configuración de la aplicación Flask
app = Flask(__name__)
CORS(app)

# ----------------------------- USUARIOS ---------------------------------
@app.route('/api/usuarios', methods=['POST'])
def registrar_usuario_route():
    data = request.get_json()
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    try:
        registrar_usuario(correo, contraseña)
        return jsonify({'message': 'Usuario registrado con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/usuarios/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    if autenticacion_de_usuario(correo, contraseña):
        return jsonify({'message': 'Autenticación exitosa'}), 200
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401

# ----------------------------- ALUMNOS ---------------------------------
@app.route('/api/alumnos', methods=['POST'])
def agregar_alumno_route():
    data = request.get_json()
    try:
        alumno = Alumno(**data)
        agregar_alumno(alumno)
        return jsonify({'message': 'Alumno agregado con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/alumnos/<ci>', methods=['DELETE'])
def eliminar_alumno_route(ci):
    try:
        eliminar_alumno(ci)
        return jsonify({'message': 'Alumno eliminado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/alumnos', methods=['GET'])
def obtener_alumnos_route():
    try:
        alumnos = obtener_todos_los_alumnos()
        return jsonify(alumnos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/alumnos/<ci>', methods=['PUT'])
def modificar_alumno_route(ci):
    data = request.get_json()
    try:
        datos_nuevos = {
            "nombre": data.get('nombre'),
            "apellido": data.get('apellido'),
            "fecha_nacimiento": data.get('fecha_nacimiento'),
            "telefono": data.get('telefono'),
            "correo_electronico": data.get('correo_electronico')
        }
        modificar_alumno(ci, datos_nuevos)
        return jsonify({'message': 'Alumno modificado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ----------------------------- INSTRUCTORES ---------------------------------
@app.route('/api/instructores', methods=['POST'])
def agregar_instructor_route():
    data = request.get_json()
    try:
        agregar_instructor(data['ci'], data['nombre'], data['apellido'])
        return jsonify({'message': 'Instructor agregado con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/instructores/<ci>', methods=['DELETE'])
def eliminar_instructor_route(ci):
    try:
        eliminar_instructor(ci)
        return jsonify({'message': 'Instructor eliminado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/instructores/<ci>', methods=['PUT'])
def modificar_instructor_route(ci):
    data = request.get_json()
    try:
        modificar_instructor(ci, {'nombre': data['nombre'], 'apellido': data['apellido']})
        return jsonify({'message': 'Instructor modificado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/instructores', methods=['GET'])
def obtener_instructores_route():
    try:
        instructores = obtener_instructores()
        return jsonify(instructores), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ----------------------------- ACTIVIDADES ---------------------------------
@app.route('/api/actividades', methods=['GET'])
def obtener_actividades_route():
    try:
        actividades = obtener_actividades()
        return jsonify(actividades), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/actividades/<int:id>', methods=['PUT'])
def modificar_actividad_route(id):
    data = request.get_json()
    try:
        modificar_actividad(id, data.get('descripcion'), data.get('costo'), data.get('edad_minima'))
        return jsonify({'message': 'Actividad modificada con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ----------------------------- TURNOS ---------------------------------
@app.route('/api/turnos', methods=['POST'])
def crear_turno_route():
    data = request.get_json()
    try:
        if 'hora_inicio' not in data or 'hora_fin' not in data:
            raise ValueError("Los campos 'hora_inicio' y 'hora_fin' son obligatorios.")

        crear_turno(data['hora_inicio'], data['hora_fin'])
        return jsonify({'message': 'Turno creado con éxito'}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno al crear turno: ' + str(e)}), 500


@app.route('/api/turnos/<int:id>', methods=['PUT'])
def modificar_turno_route(id):
    data = request.get_json()
    try:
        if 'hora_inicio' not in data or 'hora_fin' not in data:
            raise ValueError("Los campos 'hora_inicio' y 'hora_fin' son obligatorios.")

        modificar_turno(id, data['hora_inicio'], data['hora_fin'])
        return jsonify({'message': 'Turno modificado con éxito'}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno al modificar turno: ' + str(e)}), 500


@app.route('/api/turnos/<int:id>', methods=['DELETE'])
def eliminar_turno_route(id):
    try:
        eliminar_turno(id)
        return jsonify({'message': 'Turno eliminado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': 'Error interno al eliminar turno: ' + str(e)}), 500


@app.route('/api/turnos', methods=['GET'])
def obtener_turnos_route():
    try:
        turnos = obtener_todos_los_turnos()
        return jsonify(turnos), 200
    except Exception as e:
        return jsonify({'error': 'Error interno al obtener turnos: ' + str(e)}), 500

# ----------------------------- CLASES ---------------------------------
@app.route('/api/clases', methods=['GET'])
def obtener_clases_route():
    try:
        clases = obtener_clases()
        return jsonify(clases), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/clases/asignar', methods=['POST'])
def asignar_clase_route():
    data = request.get_json()
    try:
        asignar_clase(data['ci_instructor'], data['id_actividad'], data['id_turno'])
        return jsonify({'message': 'Clase asignada con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/clases/agregar-alumno', methods=['POST'])
def agregar_alumno_a_clase_route():
    data = request.get_json()
    try:
        agregar_alumno_a_clase(data['id_clase'], data['ci_alumno'], data.get('id_equipamiento'))
        return jsonify({'message': 'Alumno agregado a la clase con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/clases/quitar-alumno', methods=['POST'])
def quitar_alumno_de_clase_route():
    data = request.get_json()
    try:
        quitar_alumno_de_clase(data['id_clase'], data['ci_alumno'])
        return jsonify({'message': 'Alumno quitado de la clase con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/clases', methods=['POST'])
def crear_clase_route():
    data = request.get_json()
    try:
        crear_clase(data['ci_instructor'], data['id_actividad'], data['id_turno'])
        return jsonify({'message': 'Clase creada con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/clases/<int:id>', methods=['DELETE'])
def eliminar_clase_route(id):
    try:
        eliminar_clase(id)  # Llamar con `id`
        return jsonify({'message': 'Clase eliminada con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/clases/dictada/<int:id>', methods=['PUT'])
def actualizar_dictada_route(id):
    data = request.get_json()
    print("Datos recibidos en actualizar_dictada_route:", data)  # Log para depuración
    try:
        dictada = data.get('dictada', False)  # Por defecto será False si no se pasa
        print(f"Actualizando dictada para clase {id} a {dictada}")
        actualizar_dictada(id, dictada)
        return jsonify({'message': 'Estado de dictada actualizado con éxito'}), 200
    except Exception as e:
        print("Error en actualizar_dictada_route:", str(e))  # Log para depuración
        return jsonify({'error': str(e)}), 400
# ----------------------------- REPORTES ---------------------------------
@app.route('/api/reportes/actividad-mas-ingresos', methods=['GET'])
def get_actividad_mas_ingresos():
    try:
        result = actividad_con_mas_ingresos()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/reportes/actividad-mas-alumnos', methods=['GET'])
def get_actividad_mas_alumnos():
    try:
        result = actividad_con_mas_alumnos()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/reportes/turno-mas-clases', methods=['GET'])
def get_turno_mas_clases():
    try:
        result = turno_con_mas_clases()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



# ----------------------------- MAIN ---------------------------------
if __name__ == '__main__':
    app.run(debug=True)