import React, { useState, useEffect } from "react";
import {
    agregarInstructor,
    modificarInstructor,
    eliminarInstructor,
    obtenerInstructores,
} from "../services/api";

import "./styles.css";
import {useNavigate} from "react-router-dom";

const Instructores = () => {
    const navigate = useNavigate();
    const [instructores, setInstructores] = useState([]);
    const [nuevoInstructor, setNuevoInstructor] = useState({
        ci: "",
        nombre: "",
        apellido: "",
    });
    const [mensaje, setMensaje] = useState("");
    const [modoEdicion, setModoEdicion] = useState(null);
    const [instructorEditable, setInstructorEditable] = useState({
        ci: "",
        nombre: "",
        apellido: "",
    });

    useEffect(() => {
        const cargarInstructores = async () => {
            try {
                const data = await obtenerInstructores();
                setInstructores(data);
            } catch (error) {
                setMensaje("Error al cargar instructores");
            }
        };

        cargarInstructores();
    }, []);

    const handleAgregar = async () => {
        try {
            await agregarInstructor(nuevoInstructor);
            setMensaje("Instructor agregado con éxito");
            const data = await obtenerInstructores();
            setInstructores(data);
            setNuevoInstructor({ ci: "", nombre: "", apellido: "" });
        } catch (error) {
            setMensaje("Error al agregar instructor");
        }
    };

    const handleEliminar = async (ci) => {
        try {
            await eliminarInstructor(ci);
            setMensaje("Instructor eliminado con éxito");
            const data = await obtenerInstructores();
            setInstructores(data);
        } catch (error) {
            setMensaje("Error al eliminar instructor");
        }
    };

    const handleModificar = async () => {
        try {
            await modificarInstructor(instructorEditable.ci, {
                nombre: instructorEditable.nombre,
                apellido: instructorEditable.apellido,
            });
            setMensaje("Instructor modificado con éxito");
            const data = await obtenerInstructores();
            setInstructores(data);
            setModoEdicion(null);
        } catch (error) {
            setMensaje("Error al modificar instructor");
        }
    };

    return (
        <div className="container">
            <h1>Gestión de Instructores</h1>
            {mensaje && <p className="mensaje">{mensaje}</p>}

            {/* Tabla primero */}
            <h2>Lista de Instructores</h2>
            <table>
                <thead>
                <tr>
                    <th>CI</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Acciones</th>
                </tr>
                </thead>
                <tbody>
                {instructores.map((instructor) => (
                    <tr key={instructor.ci}>
                        {modoEdicion === instructor.ci ? (
                            <>
                                <td>{instructor.ci}</td>
                                <td>
                                    <input
                                        type="text"
                                        value={instructorEditable.nombre}
                                        onChange={(e) =>
                                            setInstructorEditable({
                                                ...instructorEditable,
                                                nombre: e.target.value,
                                            })
                                        }
                                    />
                                </td>
                                <td>
                                    <input
                                        type="text"
                                        value={instructorEditable.apellido}
                                        onChange={(e) =>
                                            setInstructorEditable({
                                                ...instructorEditable,
                                                apellido: e.target.value,
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
                                <td>{instructor.ci}</td>
                                <td>{instructor.nombre}</td>
                                <td>{instructor.apellido}</td>
                                <td>
                                    <button
                                        onClick={() => {
                                            setModoEdicion(instructor.ci);
                                            setInstructorEditable(instructor);
                                        }}
                                    >
                                        Modificar
                                    </button>
                                    <button onClick={() => handleEliminar(instructor.ci)}>
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
            <h2>Agregar Instructor</h2>
            <div className="formulario">
                <input
                    type="text"
                    placeholder="CI"
                    value={nuevoInstructor.ci}
                    onChange={(e) =>
                        setNuevoInstructor({...nuevoInstructor, ci: e.target.value})
                    }
                />
                <input
                    type="text"
                    placeholder="Nombre"
                    value={nuevoInstructor.nombre}
                    onChange={(e) =>
                        setNuevoInstructor({...nuevoInstructor, nombre: e.target.value})
                    }
                />
                <input
                    type="text"
                    placeholder="Apellido"
                    value={nuevoInstructor.apellido}
                    onChange={(e) =>
                        setNuevoInstructor({...nuevoInstructor, apellido: e.target.value})
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

export default Instructores;