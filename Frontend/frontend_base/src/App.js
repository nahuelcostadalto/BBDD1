import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Alumnos from './pages/Alumnos';
import Instructores from './pages/Instructores';
import Actividades from './pages/Actividades';
import Turnos from './pages/Turnos';
import Clases from './pages/Clases'; // Importa Clases
import Reportes from './pages/Reportes'; // Importa Reportes
import ProtectedRoute from './components/ProtectedRoute';
import Home from './pages/Home';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />} />
                {/* Rutas protegidas */}
                <Route
                    path="/alumnos"
                    element={
                        <ProtectedRoute>
                            <Alumnos />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/instructores"
                    element={
                        <ProtectedRoute>
                            <Instructores />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/actividades"
                    element={
                        <ProtectedRoute>
                            <Actividades />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/turnos"
                    element={
                        <ProtectedRoute>
                            <Turnos />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/clases"
                    element={
                        <ProtectedRoute>
                            <Clases />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/reportes" // Nueva ruta para Reportes
                    element={
                        <ProtectedRoute>
                            <Reportes />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/Home"
                    element={
                        <ProtectedRoute>
                            <Home />
                        </ProtectedRoute>
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;