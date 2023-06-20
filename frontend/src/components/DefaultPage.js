import React from 'react'
import './App.css'
import imagen1 from "/Users/sergioherrerajave/proyectdbp2023/DBP2023-1-Proyecto/frontend/src/images/clipart1363971-2 (1).png"
import { useState } from 'react';
import Userlogin from './user';

function createUser (mail, pass) {
  const data = {
    email: mail,
    password: pass
  }
  fetch('http://localhost:5001/users', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
}


export const Form = () => {
  const handleRegisterUser = () => {
    if (document.getElementById('option_usuario').checked) {
      let email = document.getElementById('email').value;
      let password = document.getElementById('password').value;
      createUser(email, password);
      alert('Usuario registrado');
      window.location.reload();
    } else if (document.getElementById('option_trainer').checked) {
      alert('Solo se pueden registrar usuarios');
    } else {
      alert('Seleccione una opcion');
    }
  };

  const handleLogin = () => {
    if (document.getElementById('option_usuario').checked) {
      window.location.href = "/User"
    }
  };

  const [renderUserLogin, setRenderUserLogin] = useState(false);
  
  return (
    <body id="body">
        <div id="form-body">
            <img id="imagen" src={imagen1} alt="user-login" />
            <p id="text">Bienvenido!</p>
            <form id="login-form">
                <input type="email" id="email" placeholder="Email"></input>
                <input type="password" id="password" placeholder="Contraseña"></input>
                <table id = "table1">
                  <tr id = "tr1">
                    <td id="td1">Trainer</td>
                    <td id="td2">
                      <input type="radio" id="option_trainer" name="radio-option" />
                    </td>
                  </tr>
                  <tr id = "tr2">
                    <td id="td1">User</td>
                    <td id="td2">
                      <input type="radio" id="option_usuario" name="radio-option" />
                    </td>
                  </tr>
                </table>
                <button type="button" onClick={handleLogin}>Iniciar Sesion</button>
                <button type="button" onClick={handleRegisterUser}>Registrar Usuario</button>
            </form>
        </div>
    </body>
  )
}

export default Form;