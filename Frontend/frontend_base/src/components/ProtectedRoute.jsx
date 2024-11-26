// Importa React para el componente funcional y Navigate para la redirección
import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
    // Verifica si el usuario está autenticado al buscar el token en localStorage
    const isAuthenticated = localStorage.getItem('token');

    // Si el usuario está autenticado, renderiza los hijos (children)
    // De lo contrario, redirige al usuario a la página de inicio ("/")
    return isAuthenticated ? children : <Navigate to="/" />;
};

export default ProtectedRoute; // Exporta el componente para ser usado en otras partes de la aplicación