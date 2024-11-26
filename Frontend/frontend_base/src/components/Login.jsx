import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUsuario } from "../services/api";
import "./Login.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const data = await loginUsuario(email, password);
      localStorage.setItem("token", data.token);
      navigate("/Home");
    } catch (err) {
      setError("Credenciales incorrectas");
    }
  };

  return (
      <div className="login-container">
        <h2>Iniciar Sesión</h2>
        <form onSubmit={handleLogin}>
          <div className="form-group">
            <label>Email:</label>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />
          </div>
          <div className="form-group">
            <label>Contraseña:</label>
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit">Iniciar Sesión</button>
        </form>
      </div>
  );
};

export default Login;