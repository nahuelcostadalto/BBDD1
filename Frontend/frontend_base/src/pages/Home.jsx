import React from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const Home = () => {
    const navigate = useNavigate();

    return (
        <div className="page-container">
            <h1 className="page-title">Bienvenido</h1>
            <p className="subtitulo">Selecciona una opción para continuar:</p>
            <div className="button-container">
                <button onClick={() => navigate("/alumnos")}>Gestión de Alumnos</button>
                <button onClick={() => navigate("/instructores")}>Gestión de Instructores</button>
                <button onClick={() => navigate("/actividades")}>Gestión de Actividades</button>
                <button onClick={() => navigate("/turnos")}>Gestión de Turnos</button>
                <button onClick={() => navigate("/clases")}>Gestión de Clases</button>
                <button onClick={() => navigate("/reportes")}>Reportes</button>
            </div>
        </div>
    );
};

export default Home;