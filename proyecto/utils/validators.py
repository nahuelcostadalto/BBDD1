# Este archivo lo vamos a utilizar para validar los datos de
# fecha de nacimiento
# validar E_mail
from datetime import datetime



def validar_fecha_nacimiento(fecha_nacimiento):
    edad = datetime.now().year - fecha_nacimiento.year
    return edad >= 18
# Nos va a devolver un True o False depende de la edad que tenga la persona
# por acuerdo vamos a definir que solo pueden ingresar a la clase personas +18
# por temas legales y ahorrar validaciones, podemos cambiarla.


def validar_email(correo):
    return "@" in correo  # Nos devuelve un True si contiene @
# y un False si no contiene @
# tenemos que hacer más validaciones dentro de la bbdd, pero usamos esta validación basica por mientras
# ya que todo correo va a tener un  @
