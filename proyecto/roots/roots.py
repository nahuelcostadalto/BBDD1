from flask import Flask, request, jsonify
from flask_cors import CORS
from services.alumnos_service import agregar_alumno, eliminar_alumno, modificar_alumno
from services.clase_service import asignar_clase, agregar_alumno_a_clase, quitar_alumno_de_clase, eliminar_clase
from services.login_service import registrar_usuario, autenticacion_de_usuario
from services.actividades_service import crear_actividad, modificar_actividad, eliminar_actividad
from services.instructor_service import agregar_instructor, eliminar_instructor, modificar_instructor
from services.reportes_services import actividad_con_mas_ingresos, actividad_con_mas_alumnos, turno_con_mas_clases
from datetime import datetime
from dominio.Alumno import Alumno
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

# Ruta para registrar usuario
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

# Ruta para autenticación de usuario
@app.route('/api/usuarios/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    if autenticacion_de_usuario(correo, contraseña):
        return jsonify({'message': 'Autenticación exitosa'}), 200
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401

# Ruta para agregar alumno
@app.route('/api/alumnos', methods=['POST'])
def agregar_alumno_route():
    data = request.get_json()
    try:
        alumno = Alumno(**data)
        agregar_alumno(alumno)
        return jsonify({'message': 'Alumno agregado con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para eliminar alumno
@app.route('/api/alumnos/<ci>', methods=['DELETE'])
def eliminar_alumno_route(ci):
    try:
        eliminar_alumno(ci)
        return jsonify({'message': 'Alumno eliminado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas para Actividades

# Ruta para crear actividad
@app.route('/api/actividades', methods=['POST'])
def crear_actividad_route():
    data = request.get_json()
    descripcion = data.get('descripcion')
    costo = data.get('costo')
    edad_minima = data.get('edad_minima')
    try:
        crear_actividad(descripcion, costo, edad_minima)
        return jsonify({'message': 'Actividad creada con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para modificar actividad
@app.route('/api/actividades/<int:id>', methods=['PUT'])
def modificar_actividad_route(id):
    data = request.get_json()
    nueva_descripcion = data.get('descripcion')
    nuevo_costo = data.get('costo')
    nueva_edad_minima = data.get('edad_minima')
    try:
        modificar_actividad(id, nueva_descripcion, nuevo_costo, nueva_edad_minima)
        return jsonify({'message': 'Actividad modificada con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para eliminar actividad
@app.route('/api/actividades/<int:id>', methods=['DELETE'])
def eliminar_actividad_route(id):
    try:
        eliminar_actividad(id)
        return jsonify({'message': 'Actividad eliminada con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    


# Rutas para Instructores

# Ruta para agregar instructor
@app.route('/api/instructores', methods=['POST'])
def agregar_instructor_route():
    data = request.get_json()
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    try:
        agregar_instructor(ci, nombre, apellido)
        return jsonify({'message': 'Instructor agregado con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para eliminar instructor
@app.route('/api/instructores/<ci>', methods=['DELETE'])
def eliminar_instructor_route(ci):
    try:
        eliminar_instructor(ci)
        return jsonify({'message': 'Instructor eliminado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para modificar instructor
@app.route('/api/instructores/<ci>', methods=['PUT'])
def modificar_instructor_route(ci):
    data = request.get_json()
    datos_nuevos = {
        "nombre": data.get('nombre'),
        "apellido": data.get('apellido')
    }
    try:
        modificar_instructor(ci, datos_nuevos)
        return jsonify({'message': 'Instructor modificado con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas para Reportes

# Ruta para obtener actividad con más ingresos
@app.route('/api/reportes/actividad-mas-ingresos', methods=['GET'])
def get_actividad_mas_ingresos():
    result = actividad_con_mas_ingresos()
    return jsonify(result)

# Ruta para obtener actividad con más alumnos
@app.route('/api/reportes/actividad-mas-alumnos', methods=['GET'])
def get_actividad_mas_alumnos():
    result = actividad_con_mas_alumnos()
    return jsonify(result)

# Ruta para obtener turno con más clases
@app.route('/api/reportes/turno-mas-clases', methods=['GET'])
def get_turno_mas_clases():
    result = turno_con_mas_clases()
    return jsonify(result)

# Rutas para clases
# Ruta para asignar clase a una actividad
@app.route('/api/clases/asignar', methods=['POST'])
def asignar_clase_route():
    data = request.get_json()
    id_actividad = data.get('id_actividad')
    descripcion_clase = data.get('descripcion_clase')
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')
    try:
        asignar_clase(id_actividad, descripcion_clase, hora_inicio, hora_fin)
        return jsonify({'message': 'Clase asignada con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para agregar un alumno a una clase
@app.route('/api/clases/agregar-alumno', methods=['POST'])
def agregar_alumno_a_clase_route():
    data = request.get_json()
    ci_alumno = data.get('ci_alumno')
    id_clase = data.get('id_clase')
    try:
        agregar_alumno_a_clase(ci_alumno, id_clase)
        return jsonify({'message': 'Alumno agregado a la clase con éxito'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para quitar un alumno de una clase
@app.route('/api/clases/quitar-alumno', methods=['POST'])
def quitar_alumno_de_clase_route():
    data = request.get_json()
    ci_alumno = data.get('ci_alumno')
    id_clase = data.get('id_clase')
    try:
        quitar_alumno_de_clase(ci_alumno, id_clase)
        return jsonify({'message': 'Alumno quitado de la clase con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ruta para eliminar una clase
@app.route('/api/clases/<int:id>', methods=['DELETE'])
def eliminar_clase_route(id):
    try:
        eliminar_clase(id)
        return jsonify({'message': 'Clase eliminada con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
# Corre la aplicación en el puerto deseado
if __name__ == '__main__':
    app.run(debug=True, port=5000)