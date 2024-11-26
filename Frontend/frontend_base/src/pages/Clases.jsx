import React, { useState, useEffect } from "react";
import {
    obtenerTurnos,
    obtenerInstructores,
    obtenerActividades,
    obtenerClases,
    asignarClase,
    eliminarClase,
    actualizarDictadaClase,
    agregarAlumnoAClase,
    quitarAlumnoDeClase,
    obtenerAlumnos,
} from "../services/api";
import { useNavigate } from "react-router-dom";
import "./styles.css";

const Clases = () => {
    const [turnos, setTurnos] = useState([]);
    const [instructores, setInstructores] = useState([]);
    const [actividades, setActividades] = useState([]);
    const [alumnos, setAlumnos] = useState([]);
    const [clases, setClases] = useState([]);
    const [nuevaClase, setNuevaClase] = useState({
        ci_instructor: "",
        id_actividad: "",
        id_turno: "",
        dictada: false,
    });
    const [alumnoClase, setAlumnoClase] = useState({ ci_alumno: "", id_clase: "" });
    const [mensaje, setMensaje] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const cargarDatos = async () => {
            try {
                console.log("Iniciando carga de datos...");

                const [turnosData, instructoresData, actividadesData, alumnosData, clasesData] =
                    await Promise.all([
                        obtenerTurnos(),
                        obtenerInstructores(),
                        obtenerActividades(),
                        obtenerAlumnos(),
                        obtenerClases(),
                    ]);

                setTurnos(turnosData);
                setInstructores(instructoresData);
                setActividades(actividadesData);
                setAlumnos(alumnosData);
                setClases(clasesData);

                console.log("Todos los datos se cargaron correctamente.");
            } catch (error) {
                console.error("Error durante la carga de datos:", error);
                setMensaje("Error al cargar datos");
            }
        };

        cargarDatos();
    }, []);

    const handleAsignarClase = async () => {
        try {
            await asignarClase(
                nuevaClase.ci_instructor,
                nuevaClase.id_actividad,
                nuevaClase.id_turno,
                nuevaClase.dictada
            );

            setMensaje("Clase asignada con éxito");
            const clasesData = await obtenerClases();
            setClases(clasesData);

            setNuevaClase({
                ci_instructor: "",
                id_actividad: "",
                id_turno: "",
                dictada: false,
            });
        } catch (error) {
            setMensaje("Error al asignar clase");
        }
    };

    const handleEliminarClase = async (id_clase) => {
        try {
            await eliminarClase(id_clase);
            const clasesData = await obtenerClases();
            setClases(clasesData);
            setMensaje("Clase eliminada con éxito");
        } catch (error) {
            console.error("Error al eliminar clase:", error);
            setMensaje("Error al eliminar clase.");
        }
    };

    const handleToggleDictada = async (id_clase, nuevaDictada) => {
        if (!id_clase) {
            setMensaje("Error: No se puede actualizar el estado de una clase sin ID.");
            return;
        }

        try {
            await actualizarDictadaClase(id_clase, nuevaDictada);
            const clasesData = await obtenerClases();
            setClases(clasesData);
            setMensaje(`Estado de 'dictada' para Clase actualizado con éxito.`);
        } catch (error) {
            console.error("Error al actualizar estado de clase dictada:", error);
            setMensaje("Error al actualizar estado de dictada.");
        }
    };

    const handleAgregarAlumnoAClase = async () => {
        try {
            await agregarAlumnoAClase(alumnoClase.ci_alumno, alumnoClase.id_clase);
            setMensaje("Alumno agregado a la clase con éxito");
        } catch (error) {
            console.error("Error al agregar alumno a la clase:", error);
            setMensaje("Error al agregar alumno a la clase");
        }
    };

    const handleQuitarAlumnoDeClase = async () => {
        try {
            await quitarAlumnoDeClase(alumnoClase.ci_alumno, alumnoClase.id_clase);
            setMensaje("Alumno quitado de la clase con éxito");
        } catch (error) {
            console.error("Error al quitar alumno de la clase:", error);
            setMensaje("Error al quitar alumno de la clase");
        }
    };

    return (
        <div className="container">
            <h1>Gestión de Clases</h1>
            {mensaje && <p className="mensaje">{mensaje}</p>}

            <h2>Lista de Clases</h2>
            <table>
                <thead>
                <tr>
                    <th>Instructor</th>
                    <th>Actividad</th>
                    <th>Turno</th>
                    <th>Dictada</th>
                    <th>Acciones</th>
                </tr>
                </thead>
                <tbody>
                {clases.map((clase) => (
                    <tr key={clase.id_clase}>
                        <td>
                            {instructores.find((instructor) => instructor.ci === clase.ci_instructor)?.nombre ||
                                "Desconocido"}
                        </td>
                        <td>
                            {actividades.find((actividad) => actividad.id === clase.id_actividad)?.descripcion ||
                                "Desconocida"}
                        </td>
                        <td>
                            {turnos.find((turno) => turno.id === clase.id_turno)?.hora_inicio} -{" "}
                            {turnos.find((turno) => turno.id === clase.id_turno)?.hora_fin}
                        </td>
                        <td>
                            <input
                                type="checkbox"
                                checked={clase.dictada}
                                onChange={() =>
                                    handleToggleDictada(clase.id_clase, !clase.dictada)
                                }
                            />
                        </td>
                        <td>
                            <button onClick={() => handleEliminarClase(clase.id_clase)}>Eliminar</button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>

            <h2>Agregar o Quitar Alumno de Clase</h2>
            <div className="formulario">
                <select
                    value={alumnoClase.ci_alumno}
                    onChange={(e) => setAlumnoClase({ ...alumnoClase, ci_alumno: e.target.value })}
                >
                    <option value="">Seleccionar Alumno</option>
                    {alumnos.map((alumno) => (
                        <option key={alumno.ci} value={alumno.ci}>
                            {alumno.nombre} {alumno.apellido}
                        </option>
                    ))}
                </select>
                <select
                    value={alumnoClase.id_clase}
                    onChange={(e) => setAlumnoClase({ ...alumnoClase, id_clase: e.target.value })}
                >
                    <option value="">Seleccionar Clase</option>
                    {clases.map((clase) => (
                        <option key={clase.id_clase} value={clase.id_clase}>
                            {instructores.find((inst) => inst.ci === clase.ci_instructor)?.nombre || "Desconocido"}
                        </option>
                    ))}
                </select>
                <button onClick={handleAgregarAlumnoAClase}>Agregar Alumno</button>
                <button onClick={handleQuitarAlumnoDeClase}>Quitar Alumno</button>
            </div>

            <h2>Asignar Clase</h2>
            <div className="formulario">
                <select
                    value={nuevaClase.ci_instructor}
                    onChange={(e) => setNuevaClase({ ...nuevaClase, ci_instructor: e.target.value })}
                >
                    <option value="">Seleccionar Instructor</option>
                    {instructores.map((instructor) => (
                        <option key={instructor.ci} value={instructor.ci}>
                            {instructor.nombre} {instructor.apellido}
                        </option>
                    ))}
                </select>
                <select
                    value={nuevaClase.id_actividad}
                    onChange={(e) => setNuevaClase({ ...nuevaClase, id_actividad: e.target.value })}
                >
                    <option value="">Seleccionar Actividad</option>
                    {actividades.map((actividad) => (
                        <option key={actividad.id} value={actividad.id}>
                            {actividad.descripcion}
                        </option>
                    ))}
                </select>
                <select
                    value={nuevaClase.id_turno}
                    onChange={(e) => setNuevaClase({ ...nuevaClase, id_turno: e.target.value })}
                >
                    <option value="">Seleccionar Turno</option>
                    {turnos.map((turno) => (
                        <option key={turno.id} value={turno.id}>
                            {turno.hora_inicio} - {turno.hora_fin}
                        </option>
                    ))}
                </select>
                <button onClick={handleAsignarClase}>Asignar Clase</button>
            </div>

            <div className="boton-container">
                <button className="volver" onClick={() => navigate("/Home")}>
                    Volver a Home
                </button>
            </div>
        </div>
    );
};

export default Clases;