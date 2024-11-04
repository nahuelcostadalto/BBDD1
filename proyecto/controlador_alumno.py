from flask import Flask, request, jsonify
from services.alumnos_service import agregar_alumno
from datetime import datetime
from dominio import Alumno

app = Flask(__name__)
#parte de esto va a ser mi main, donde defino Flask va en el main junto a las rutas.


@app.route('/agregar_alumno', methods=['POST'])

def agregar_alumno_endpoint():
    # Obtener datos en JSON desde la solicitud
    datos = request.get_json()

    # Crear el objeto Alumno utilizando los datos recibidos
    try:
        alumno = Alumno(
            ci=datos["ci"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            fecha_nacimiento=datos["fecha_nacimiento"],  # La conversión se maneja en el setter
            telefono=datos["telefono"],
            correo_electronico=datos["correo_electronico"]
        )

        # Agregar el alumno a la base de datos usando `agregar_alumno`
        agregar_alumno(
            alumno.ci,
            alumno.nombre,
            alumno.apellido,
            alumno.fecha_nacimiento,
            alumno.telefono,
            alumno.correo_electronico
        )

        return jsonify({"message": "Alumno agregado correctamente", "alumno": repr(alumno)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
