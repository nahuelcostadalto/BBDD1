import React, { useState, useEffect } from "react";
import { obtenerActividades, modificarActividad } from "../services/api";
import "./styles.css";
import { useNavigate } from "react-router-dom";

const Actividades = () => {
  const [actividades, setActividades] = useState([]);
  const [mensaje, setMensaje] = useState("");
  const [modoEdicion, setModoEdicion] = useState(null);
  const navigate = useNavigate();
  const [actividadEditable, setActividadEditable] = useState({
    descripcion: "",
    costo: "",
    edad_minima: "",
  });

  useEffect(() => {
    const cargarActividades = async () => {
      try {
        const data = await obtenerActividades();
        setActividades(data);
      } catch (error) {
        setMensaje("Error al cargar actividades");
      }
    };

    cargarActividades();
  }, []);

  const handleModificar = async () => {
    try {
      await modificarActividad(actividadEditable.id, {
        descripcion: actividadEditable.descripcion,
        costo: actividadEditable.costo,
        edad_minima: actividadEditable.edad_minima,
      });
      setMensaje("Actividad modificada con éxito");
      const data = await obtenerActividades();
      setActividades(data);
      setModoEdicion(null);
    } catch (error) {
      setMensaje("Error al modificar actividad");
    }
  };

  return (
      <div className="container">
        <h1>Gestión de Actividades</h1>
        {mensaje && <p className="mensaje">{mensaje}</p>}

        {/* Tabla para mostrar y modificar actividades */}
        <h2>Lista de Actividades</h2>
        <table>
          <thead>
          <tr>
            <th>Descripción</th>
            <th>Costo</th>
            <th>Edad Mínima</th>
            <th>Acciones</th>
          </tr>
          </thead>
          <tbody>
          {actividades.map((actividad) => (
              <tr key={actividad.id}>
                {modoEdicion === actividad.id ? (
                    <>
                      <td>
                        <input
                            type="text"
                            value={actividadEditable.descripcion}
                            onChange={(e) =>
                                setActividadEditable({
                                  ...actividadEditable,
                                  descripcion: e.target.value,
                                })
                            }
                        />
                      </td>
                      <td>
                        <input
                            type="number"
                            step="0.01"
                            value={actividadEditable.costo}
                            onChange={(e) =>
                                setActividadEditable({
                                  ...actividadEditable,
                                  costo: e.target.value,
                                })
                            }
                        />
                      </td>
                      <td>
                        <input
                            type="number"
                            value={actividadEditable.edad_minima}
                            onChange={(e) =>
                                setActividadEditable({
                                  ...actividadEditable,
                                  edad_minima: e.target.value,
                                })
                            }
                        />
                      </td>
                      <td>
                        <button onClick={handleModificar}>Guardar</button>
                        <button onClick={() => setModoEdicion(null)}>Cancelar</button>
                      </td>
                    </>
                ) : (
                    <>
                      <td>{actividad.descripcion}</td>
                      <td>${actividad.costo}</td>
                      <td>{actividad.edad_minima}</td>
                      <td>
                        <button
                            onClick={() => {
                              setModoEdicion(actividad.id);
                              setActividadEditable(actividad);
                            }}
                        >
                          Modificar
                        </button>
                      </td>
                    </>
                )}
              </tr>
          ))}
          </tbody>
        </table>

        <div className="boton-container">
          <button className="volver" onClick={() => navigate("/Home")}>
            Volver a Home
          </button>
        </div>
      </div>
  );
};

export default Actividades;