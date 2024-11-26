import React, { useState, useEffect } from "react";
import {
  crearTurno,
  modificarTurno,
  eliminarTurno,
  obtenerTurnos,
} from "../services/api";
import { useNavigate } from "react-router-dom";
import "./styles.css"; // Importa los estilos compartidos

const Turnos = () => {
  const [turnos, setTurnos] = useState([]);
  const [nuevoTurno, setNuevoTurno] = useState({
    hora_inicio: "",
    hora_fin: "",
  });
  const [mensaje, setMensaje] = useState("");
  const [modoEdicion, setModoEdicion] = useState(null);
  const [turnoEditable, setTurnoEditable] = useState({
    id: "",
    hora_inicio: "",
    hora_fin: "",
  });

  const navigate = useNavigate();

  useEffect(() => {
    const cargarTurnos = async () => {
      try {
        const data = await obtenerTurnos();
        setTurnos(data);
      } catch (error) {
        setMensaje("Error al cargar turnos");
      }
    };

    cargarTurnos();
  }, []);

  const handleAgregar = async () => {
    if (!nuevoTurno.hora_inicio || !nuevoTurno.hora_fin) {
      setMensaje("Ambos campos de hora son obligatorios.");
      return;
    }

    try {
      await crearTurno(nuevoTurno);
      setMensaje("Turno creado con éxito");
      const data = await obtenerTurnos();
      setTurnos(data);
      setNuevoTurno({ hora_inicio: "", hora_fin: "" });
    } catch (error) {
      setMensaje("Error al crear turno");
    }
  };

  const handleModificar = async () => {
    if (!turnoEditable.hora_inicio || !turnoEditable.hora_fin) {
      setMensaje("Ambos campos de hora son obligatorios.");
      return;
    }

    try {
      await modificarTurno(turnoEditable.id, turnoEditable);
      setMensaje("Turno modificado con éxito");
      const data = await obtenerTurnos();
      setTurnos(data);
      setModoEdicion(null);
    } catch (error) {
      setMensaje("Error al modificar turno");
    }
  };

  const handleEliminar = async (id) => {
    try {
      await eliminarTurno(id);
      setMensaje("Turno eliminado con éxito");
      const data = await obtenerTurnos();
      setTurnos(data);
    } catch (error) {
      setMensaje("Error al eliminar turno");
    }
  };

  return (
    <div className="container">
      <h1>Gestión de Turnos</h1>
      {mensaje && <p className="mensaje">{mensaje}</p>}

      {/* Tabla de turnos */}
      <h2>Lista de Turnos</h2>
      <table>
        <thead>
          <tr>
            <th>Hora de Inicio</th>
            <th>Hora de Fin</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {turnos.map((turno) => (
            <tr key={turno.id}>
              {modoEdicion === turno.id ? (
                <>
                  <td>
                    <input
                      type="time"
                      value={turnoEditable.hora_inicio}
                      onChange={(e) =>
                        setTurnoEditable({
                          ...turnoEditable,
                          hora_inicio: e.target.value,
                        })
                      }
                      step="60" // Asegura intervalos de minutos
                      min="00:00" // Hora mínima permitida
                      max="23:59" // Hora máxima permitida
                    />
                  </td>
                  <td>
                    <input
                      type="time"
                      value={turnoEditable.hora_fin}
                      onChange={(e) =>
                        setTurnoEditable({
                          ...turnoEditable,
                          hora_fin: e.target.value,
                        })
                      }
                      step="60"
                      min="00:00"
                      max="23:59"
                    />
                  </td>
                  <td>
                    <button onClick={handleModificar}>Guardar</button>
                    <button onClick={() => setModoEdicion(null)}>Cancelar</button>
                  </td>
                </>
              ) : (
                <>
                  <td>{turno.hora_inicio}</td>
                  <td>{turno.hora_fin}</td>
                  <td>
                    <button
                      onClick={() => {
                        setModoEdicion(turno.id);
                        setTurnoEditable(turno);
                      }}
                    >
                      Modificar
                    </button>
                    <button onClick={() => handleEliminar(turno.id)}>
                      Eliminar
                    </button>
                  </td>
                </>
              )}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Formulario para agregar turnos */}
      <h2>Agregar Turno</h2>
      <div className="formulario">
        <input
          type="time"
          value={nuevoTurno.hora_inicio}
          onChange={(e) =>
            setNuevoTurno({ ...nuevoTurno, hora_inicio: e.target.value })
          }
          step="60"
          min="00:00"
          max="23:59"
        />
        <input
          type="time"
          value={nuevoTurno.hora_fin}
          onChange={(e) =>
            setNuevoTurno({ ...nuevoTurno, hora_fin: e.target.value })
          }
          step="60"
          min="00:00"
          max="23:59"
        />
        <button onClick={handleAgregar}>Agregar Turno</button>
      </div>
    </div>
  );
};

export default Turnos;