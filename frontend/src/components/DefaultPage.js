import React from 'react'
import './App.css'
import imagen1 from "/Users/sergioherrerajave/proyectdbp2023/DBP2023-1-Proyecto/frontend/src/images/clipart1363971-2 (1).png"

export const Form = () => {
  const handleRegisterUser = () => {
    if(document.getElementById('radio-option-1').checked)
    window.open('/Users/sergioherrerajave/proyectdbp2023/DBP2023-1-Proyecto/frontend/build/static/js', '_blank');
    alert('Usuario registrado');
  }
  return (
    <body id="body">
        <div id="form-body">
            <img id="imagen" src={imagen1} alt="user-login" />
            <p id="text">Bienvenido!</p>
            <form id="login-form">
                <input type="email" placeholder="Email"></input>
                <input type="password" placeholder="Contraseña"></input>
                <table id = "table1">
                  <tr id = "tr1">
                    <td id="td1">Trainer</td>
                    <td id="td2">
                      <input type="radio" id="radio-option-1" name="radio-option" />
                    </td>
                  </tr>
                  <tr id = "tr2">
                    <td id="td1">User</td>
                    <td id="td2">
                      <input type="radio" id="radio-option-2" name="radio-option" />
                    </td>
                  </tr>
                </table>
                <button>Iniciar Sesion</button>
                <button type="button" onClick={handleRegisterUser}>Registrar Usuario</button>
            </form>
        </div>
    </body>
  )
}
export default Form;