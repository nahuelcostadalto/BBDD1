from datetime import datetime, date
#class Alumno sir
def convertir_fecha(fecha_nacimiento): #sacar esta def de la clase
    print("fechiña")
    if isinstance(fecha_nacimiento, str):
        return datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    elif isinstance(fecha_nacimiento, date):
        return fecha_nacimiento
    else:
        raise ValueError("fecha_nacimiento debe ser una cadena en formato 'YYYY-MM-DD' o un objeto date")

class Alumno: #nunca se crea el objeto ya que no entra al Alumno=alimno
    def __init__(self, ci, nombre, apellido, fecha_nacimiento, telefono, correo_electronico):
        
        self.ci = ci
        print(self.ci)
        self.nombre = nombre
        print(self.nombre)
        self.apellido = apellido
        print(self.apellido)
        self.fecha_nacimiento = convertir_fecha(fecha_nacimiento)
        print(self.fecha_nacimiento)
        self.telefono = telefono
        print(self.telefono)

        self.correo_electronico = correo_electronico
        print(self.correo_electronico)
    

    
    def es_mayor_de_edad(self):
        return (date.today().year - self.fecha_nacimiento.year) >= 18

    def __repr__(self):
        return (f"Alumno(ci={self.ci}, nombre={self.nombre}, apellido={self.apellido}, "
                f"fecha_nacimiento={self.fecha_nacimiento}, telefono={self.telefono}, "
                f"correo_electronico={self.correo_electronico})")
