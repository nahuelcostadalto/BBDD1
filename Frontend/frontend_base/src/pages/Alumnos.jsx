import React, { useState, useEffect } from "react";
import {
    agregarAlumno,
    modificarAlumno,
    eliminarAlumno,
    obtenerAlumnos,
} from "../services/api";
import { useNavigate} from "react-router-dom";
import "./styles.css";

const Alumnos = () => {
    const navigate = useNavigate();
    const [alumnos, setAlumnos] = useState([]);
    const [nuevoAlumno, setNuevoAlumno] = useState({
        ci: "",
        nombre: "",
        apellido: "",
        fecha_nacimiento: "",
        telefono: "",
        correo_electronico: "",
    });
    const [mensaje, setMensaje] = useState("");
    const [modoEdicion, setModoEdicion] = useState(null);
    const [alumnoEditable, setAlumnoEditable] = useState({
        ci: "",
        nombre: "",
        apellido: "",
        fecha_nacimiento: "",
        telefono: "",
        correo_electronico: "",
    });

    useEffect(() => {
        const cargarAlumnos = async () => {
            try {
                const data = await obtenerAlumnos();
                setAlumnos(data);
            } catch (error) {
                setMensaje("Error al cargar alumnos");
            }
        };

        cargarAlumnos();
    }, []);

    const handleAgregar = async () => {
        try {
            await agregarAlumno(nuevoAlumno);
            setMensaje("Alumno agregado con éxito");
            const data = await obtenerAlumnos();
            setAlumnos(data);
            setNuevoAlumno({
                ci: "",
                nombre: "",
                apellido: "",
                fecha_nacimiento: "",
                telefono: "",
                correo_electronico: "",
            });
        } catch (error) {
            setMensaje("Error al agregar alumno");
        }
    };

    const handleEliminar = async (ci) => {
        try {
            await eliminarAlumno(ci);
            setMensaje("Alumno eliminado con éxito");
            const data = await obtenerAlumnos();
            setAlumnos(data);
        } catch (error) {
            setMensaje("Error al eliminar alumno");
        }
    };

    const handleModificar = async () => {
        try {
            await modificarAlumno(alumnoEditable.ci, {
                nombre: alumnoEditable.nombre,
                apellido: alumnoEditable.apellido,
                fecha_nacimiento: alumnoEditable.fecha_nacimiento,
                telefono: alumnoEditable.telefono,
                correo_electronico: alumnoEditable.correo_electronico,
            });
            setMensaje("Alumno modificado con éxito");
            const data = await obtenerAlumnos();
            setAlumnos(data);
            setModoEdicion(null);
        } catch (error) {
            setMensaje("Error al modificar alumno");
        }
    };

    return (
        <div className="container">
            <h1>Gestión de Alumnos</h1>
            {mensaje && <p className="mensaje">{mensaje}</p>}

            {/* Tabla primero */}
            <h2>Lista de Alumnos</h2>
            <table>
                <thead>
                <tr>
                    <th>CI</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Fecha Nacimiento</th>
                    <th>Teléfono</th>
                    <th>Correo Electrónico</th>
                    <th>Acciones</th>
                </tr>
                </thead>
                <tbody>
                {alumnos.map((alumno) => (
                    <tr key={alumno.ci}>
                        {modoEdicion === alumno.ci ? (
                            <>
                                <td>{alumno.ci}</td>
                                <td>
                                    <input
                                        type="text"
                                        value={alumnoEditable.nombre}
                                        onChange={(e) =>
                                            setAlumnoEditable({
                                                ...alumnoEditable,
                                                nombre: e.target.value,
                                            })
                                        }
                                    />
                                </td>
                                <td>
                                    <input
                                        type="text"
                                        value={alumnoEditable.apellido}
                                        onChange={(e) =>
                                            setAlumnoEditable({
                                                ...alumnoEditable,
                                                apellido: e.target.value,
                                            })
                                        }
                                    />
                                </td>
                                <td>
                                    <input
                                        type="date"
                                        value={alumnoEditable.fecha_nacimiento}
                                        onChange={(e) =>
                                            setAlumnoEditable({
                                                ...alumnoEditable,
                                                fecha_nacimiento: e.target.value,
                                            })
                                        }
                                    />
                                </td>
                                <td>
                                    <input
                                        type="text"
                                        value={alumnoEditable.telefono}
                                        onChange={(e) =>
                                            setAlumnoEditable({
                                                ...alumnoEditable,
                                                telefono: e.target.value,
                                            })
                                        }
                                    />
                                </td>
                                <td>
                                    <input
                                        type="email"
                                        value={alumnoEditable.correo_electronico}
                                        onChange={(e) =>
                                            setAlumnoEditable({
                                                ...alumnoEditable,
                                                correo_electronico: e.target.value,
                                            })
                                        }
                                    />
                                </td>
                                <td>
                                    <button onClick={handleModificar}>Guardar</button>
                                    <button onClick={() => setModoEdicion(null)}>
                                        Cancelar
                                    </button>
                                </td>
                            </>
                        ) : (
                            <>
                                <td>{alumno.ci}</td>
                                <td>{alumno.nombre}</td>
                                <td>{alumno.apellido}</td>
                                <td>{alumno.fecha_nacimiento}</td>
                                <td>{alumno.telefono}</td>
                                <td>{alumno.correo_electronico}</td>
                                <td>
                                    <button
                                        onClick={() => {
                                            setModoEdicion(alumno.ci);
                                            setAlumnoEditable(alumno);
                                        }}
                                    >
                                        Modificar
                                    </button>
                                    <button onClick={() => handleEliminar(alumno.ci)}>
                                        Eliminar
                                    </button>
                                </td>
                            </>
                        )}
                    </tr>
                ))}
                </tbody>
            </table>

            {/* Formulario después */}
            <h2>Agregar Alumno</h2>
            <div className="formulario">
                <input
                    type="text"
                    placeholder="CI"
                    value={nuevoAlumno.ci}
                    onChange={(e) =>
                        setNuevoAlumno({...nuevoAlumno, ci: e.target.value})
                    }
                />
                <input
                    type="text"
                    placeholder="Nombre"
                    value={nuevoAlumno.nombre}
                    onChange={(e) =>
                        setNuevoAlumno({...nuevoAlumno, nombre: e.target.value})
                    }
                />
                <input
                    type="text"
                    placeholder="Apellido"
                    value={nuevoAlumno.apellido}
                    onChange={(e) =>
                        setNuevoAlumno({...nuevoAlumno, apellido: e.target.value})
                    }
                />
                <input
                    type="date"
                    placeholder="Fecha de Nacimiento"
                    value={nuevoAlumno.fecha_nacimiento}
                    onChange={(e) =>
                        setNuevoAlumno({
                            ...nuevoAlumno,
                            fecha_nacimiento: e.target.value,
                        })
                    }
                />
                <input
                    type="text"
                    placeholder="Teléfono"
                    value={nuevoAlumno.telefono}
                    onChange={(e) =>
                        setNuevoAlumno({...nuevoAlumno, telefono: e.target.value})
                    }
                />
                <input
                    type="email"
                    placeholder="Correo Electrónico"
                    value={nuevoAlumno.correo_electronico}
                    onChange={(e) =>
                        setNuevoAlumno({
                            ...nuevoAlumno,
                            correo_electronico: e.target.value,
                        })
                    }
                />
                <button onClick={handleAgregar}>Agregar</button>
            </div>

            <div className="boton-container">
                <button className="volver" onClick={() => navigate("/Home")}>
                    Volver a Home
                </button>
            </div>
        </div>
    );
};

export default Alumnos;