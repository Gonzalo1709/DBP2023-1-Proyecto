import React from 'react'
import './App.css'
import imagen1 from "/Users/sergioherrerajave/proyectodbp/src/images/clipart1363971-2 (1).png"

export const Form = () => {
  return (
    <body id="body">
        <div id="form-body">
            <img id="imagen" src={imagen1} alt="user-login" />
            <p id="text">Bienvenido!</p>
            <form class="login-form">
                <input type="email" placeholder="Email"></input>
                <input type="password" placeholder="Contraseña"></input>
                <div id="radio-div">
                  <label for="radio-option-1">Trainer</label>
                  <input type="radio" id="radio-option-1" name="radio-option" />
                  <label for="radio-option-2">User</label>
                  <input type="radio" id="radio-option-2" name="radio-option" />
                </div>
                <button>Iniciar Sesion</button>
            </form>
        </div>
    </body>
  )
}
export default Form;