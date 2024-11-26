import React, { useState, useEffect } from "react";
import {
    obtenerActividadMasIngresos,
    obtenerActividadMasAlumnos,
    obtenerTurnoMasClases,
} from "../services/api";
import { useNavigate } from "react-router-dom";
import "./styles.css";

const Reportes = () => {
    const [actividadMasIngresos, setActividadMasIngresos] = useState(null);
    const [actividadMasAlumnos, setActividadMasAlumnos] = useState(null);
    const [turnoMasClases, setTurnoMasClases] = useState(null);
    const [mensaje, setMensaje] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const cargarReportes = async () => {
            try {
                console.log("Cargando reportes...");

                const ingresos = await obtenerActividadMasIngresos();
                console.log("Actividad con más ingresos:", ingresos);

                const alumnos = await obtenerActividadMasAlumnos();
                console.log("Actividad con más alumnos:", alumnos);

                const turno = await obtenerTurnoMasClases();
                console.log("Turno con más clases:", turno);

                setActividadMasIngresos(ingresos);
                setActividadMasAlumnos(alumnos);
                setTurnoMasClases(turno);

                setMensaje("Reportes cargados correctamente.");
            } catch (error) {
                console.error("Error al cargar reportes:", error);
                setMensaje("Error al cargar reportes.");
            }
        };

        cargarReportes();
    }, []);

    return (
        <div className="container">
            <h1>Reportes</h1>
            {mensaje && <p className="mensaje">{mensaje}</p>}

            <div className="reportes">
                <h2>Actividad con más ingresos</h2>
                {actividadMasIngresos ? (
                    <p>
                        <strong>Actividad:</strong> {actividadMasIngresos.actividad || "N/A"} <br />
                        <strong>Ingresos:</strong> ${parseFloat(actividadMasIngresos.ingresos || 0).toFixed(2)}
                    </p>
                ) : (
                    <p>Cargando...</p>
                )}

                <h2>Actividad con más alumnos</h2>
                {actividadMasAlumnos ? (
                    <p>
                        <strong>Actividad:</strong> {actividadMasAlumnos.descripcion || "N/A"} <br />
                        <strong>Alumnos:</strong> {actividadMasAlumnos.total_alumnos || 0}
                    </p>
                ) : (
                    <p>Cargando...</p>
                )}

                <h2>Turno con más clases</h2>
                {turnoMasClases ? (
                    <p>
                        <strong>Turno:</strong> {turnoMasClases.hora_inicio || "N/A"} - {turnoMasClases.hora_fin || "N/A"} <br />
                        <strong>Docente:</strong> {turnoMasClases.docente || "N/A"} <br />
                        <strong>Clases:</strong> {turnoMasClases.total_clases || 0}
                    </p>
                ) : (
                    <p>Cargando...</p>
                )}
            </div>

            <div className="boton-container">
                <button className="volver" onClick={() => navigate("/Home")}>
                    Volver a Home
                </button>
            </div>
        </div>
    );
};

export default Reportes;