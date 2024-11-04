from datetime import datetime, date

class Alumno:
    def __init__(self, ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = self.convertir_fecha(fecha_nacimiento)
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    
    def convertir_fecha(self, fecha_nacimiento):
        if isinstance(fecha_nacimiento, str):
            return datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        elif isinstance(fecha_nacimiento, date):
            return fecha_nacimiento
        else:
            raise ValueError("fecha_nacimiento debe ser una cadena en formato 'YYYY-MM-DD' o un objeto date")

    
    def es_mayor_de_edad(self):
        return (date.today().year - self.fecha_nacimiento.year) >= 18

    def __repr__(self):
        return (f"Alumno(ci={self.ci}, nombre={self.nombre}, apellido={self.apellido}, "
                f"fecha_nacimiento={self.fecha_nacimiento}, telefono={self.telefono}, "
                f"correo_electronico={self.correo_electronico})")
