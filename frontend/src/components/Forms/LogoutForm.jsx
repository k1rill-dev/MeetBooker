import React from 'react';
import {Navigate} from "react-router-dom";

const logoutUser = async () => {
    return null
}

const LogoutForm = () => {
    logoutUser();
    localStorage.clear();
    return (
        <div><Navigate to="/"/></div>
    )

};

export default LogoutForm;