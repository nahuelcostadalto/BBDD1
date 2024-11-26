const API_URL = "http://127.0.0.1:5000/api"; // Dirección base de tu backend Flask


// Helper para configurar headers con token
const getAuthHeaders = () => {
  const token = localStorage.getItem("token");
  return {
    "Content-Type": "application/json",
    Authorization: token ? `Bearer ${token}` : "",
  };
};

// ----------------------------- USUARIOS ---------------------------------
// Función para autenticar un usuario
export const loginUsuario = async (correo, contraseña) => {
  try {
    const response = await fetch(`${API_URL}/usuarios/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ correo, contraseña }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Credenciales incorrectas");
    }

    // Guardar el token en el almacenamiento local después del login
    const data = await response.json();
    localStorage.setItem("token", data.token);
    return data;
  } catch (error) {
    console.error("Error en loginUsuario:", error);
    throw error;
  }
};
// ----------------------------- ALUMNOS ---------------------------------
// Función para agregar un alumno
export const agregarAlumno = async (alumno) => {
  try {
    const response = await fetch(`${API_URL}/alumnos`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify(alumno),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al agregar alumno");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en agregarAlumno:", error);
    throw error;
  }
};

// Función para eliminar un alumno
export const eliminarAlumno = async (ci) => {
  try {
    const response = await fetch(`${API_URL}/alumnos/${ci}`, {
      method: "DELETE",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al eliminar alumno");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en eliminarAlumno:", error);
    throw error;
  }
};
// Función para obtener todos los alumnos
export const obtenerAlumnos = async () => {
  try {
    const response = await fetch(`${API_URL}/alumnos`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al obtener alumnos");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerAlumnos:", error);
    throw error;
  }
};

// Función para modificar un alumno
export const modificarAlumno = async (ci, datosNuevos) => {
  try {
    const response = await fetch(`${API_URL}/alumnos/${ci}`, {
      method: "PUT",
      headers: getAuthHeaders(),
      body: JSON.stringify(datosNuevos),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al modificar alumno");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en modificarAlumno:", error);
    throw error;
  }
};

// ----------------------------- INSTRUCTORES ---------------------------------
// Agregar un instructor
export const agregarInstructor = async (instructor) => {
  try {
    const response = await fetch(`${API_URL}/instructores`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify(instructor),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al agregar instructor");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en agregarInstructor:", error);
    throw error;
  }
};

// Modificar un instructor
export const modificarInstructor = async (ci, datosNuevos) => {
  try {
    const response = await fetch(`${API_URL}/instructores/${ci}`, {
      method: "PUT",
      headers: getAuthHeaders(),
      body: JSON.stringify(datosNuevos),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al modificar instructor");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en modificarInstructor:", error);
    throw error;
  }
};

// Eliminar un instructor
export const eliminarInstructor = async (ci) => {
  try {
    const response = await fetch(`${API_URL}/instructores/${ci}`, {
      method: "DELETE",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al eliminar instructor");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en eliminarInstructor:", error);
    throw error;
  }
};

// Función para obtener todos los instructores
export const obtenerInstructores = async () => {
  try {
    const response = await fetch(`${API_URL}/instructores`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al obtener instructores");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerInstructores:", error);
    throw error;
  }
};





// Actividades
// Función para modificar una actividad
export const modificarActividad = async (id, nuevaActividad) => {
  try {
    const response = await fetch(`${API_URL}/actividades/${id}`, {
      method: "PUT",
      headers: getAuthHeaders(),
      body: JSON.stringify(nuevaActividad),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al modificar actividad");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en modificarActividad:", error);
    throw error;
  }
};

// ----------------------------- ACTIVIDADES ---------------------------------
// Función para obtener todas las actividades
export const obtenerActividades = async () => {
  try {
    const response = await fetch(`${API_URL}/actividades`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al obtener actividades");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerActividades:", error);
    throw error;
  }
};


// ----------------------------- TURNOS ---------------------------------

// Turnos
// Función para crear un turno
export const crearTurno = async (turno) => {
  try {
    const response = await fetch(`${API_URL}/turnos`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify(turno),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al crear turno");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en crearTurno:", error);
    throw error;
  }
};

// Función para modificar un turno
export const modificarTurno = async (id, nuevosDatos) => {
  try {
    const response = await fetch(`${API_URL}/turnos/${id}`, {
      method: "PUT",
      headers: getAuthHeaders(),
      body: JSON.stringify(nuevosDatos),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al modificar turno");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en modificarTurno:", error);
    throw error;
  }
};

// Función para eliminar un turno
export const eliminarTurno = async (id) => {
  try {
    const response = await fetch(`${API_URL}/turnos/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al eliminar turno");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en eliminarTurno:", error);
    throw error;
  }
};

// Función para obtener todos los turnos
export const obtenerTurnos = async () => {
  try {
    const response = await fetch(`${API_URL}/turnos`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al obtener turnos");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerTurnos:", error);
    throw error;
  }
};

// ----------------------------- CLASES ---------------------------------
// Función para obtener todas las clases
export const obtenerClases = async () => {
  try {
    const response = await fetch(`${API_URL}/clases`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al obtener clases");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerClases:", error);
    throw error;
  }
};
// Función para asignar una clase a una actividad
export const asignarClase = async (ci_instructor, id_actividad, id_turno) => {
  try {
    const response = await fetch(`${API_URL}/clases/asignar`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({ ci_instructor, id_actividad, id_turno }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al asignar clase");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en asignarClase:", error);
    throw error;
  }
};

// Función para agregar un alumno a una clase
export const agregarAlumnoAClase = async (ci_alumno, id_clase) => {
  try {
    const response = await fetch(`${API_URL}/clases/agregar-alumno`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({ ci_alumno, id_clase }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al agregar alumno a la clase");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en agregarAlumnoAClase:", error);
    throw error;
  }
};

// Función para quitar un alumno de una clase
export const quitarAlumnoDeClase = async (ci_alumno, id_clase) => {
  try {
    const response = await fetch(`${API_URL}/clases/quitar-alumno`, {
      method: "POST",
      headers: getAuthHeaders(),
      body: JSON.stringify({ ci_alumno, id_clase }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al quitar alumno de la clase");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en quitarAlumnoDeClase:", error);
    throw error;
  }
};

// Función para eliminar una clase
export const eliminarClase = async (id_clase) => {
  try {
    const response = await fetch(`${API_URL}/clases/${id_clase}`, {
      method: "DELETE",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al eliminar clase");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en eliminarClase:", error);
    throw error;
  }
};
// Función para actualizar el estado de dictada de una clase
export const actualizarDictadaClase = async (id_clase, dictada) => {
  try {
    const response = await fetch(`${API_URL}/clases/dictada/${id_clase}`, {
      method: "PUT",
      headers: getAuthHeaders(),
      body: JSON.stringify({ dictada }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al actualizar estado de dictada");
    }
    return await response.json();
  } catch (error) {
    console.error("Error en actualizarDictadaClase:", error);
    throw error;
  }
};


// ----------------------------- REPORTES ---------------------------------

// Función para obtener la actividad con más ingresos
export const obtenerActividadMasIngresos = async () => {
  try {
    const response = await fetch(`${API_URL}/reportes/actividad-mas-ingresos`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(
          errorData.error || "Error al obtener actividad con más ingresos"
      );
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerActividadMasIngresos:", error);
    throw error;
  }
};

// Función para obtener la actividad con más alumnos
export const obtenerActividadMasAlumnos = async () => {
  try {
    const response = await fetch(`${API_URL}/reportes/actividad-mas-alumnos`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(
          errorData.error || "Error al obtener actividad con más alumnos"
      );
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerActividadMasAlumnos:", error);
    throw error;
  }
};

// Función para obtener el turno con más clases
export const obtenerTurnoMasClases = async () => {
  try {
    const response = await fetch(`${API_URL}/reportes/turno-mas-clases`, {
      method: "GET",
      headers: getAuthHeaders(),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(
          errorData.error || "Error al obtener turno con más clases"
      );
    }
    return await response.json();
  } catch (error) {
    console.error("Error en obtenerTurnoMasClases:", error);
    throw error;
  }
};