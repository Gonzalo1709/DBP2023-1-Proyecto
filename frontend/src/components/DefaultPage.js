import React from 'react'
import './App.css'
import imagen1 from '../images/clipart1363971-2 (1).png'
import { useState } from 'react';
import Userlogin from './user';



function createUser (mail, pass) {
  let data = {
    email: mail,
    password: pass
  }
  fetch('http://localhost:5001/users', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(response => response.json()).then(response =>{ // Se tiene que hacer then dos veces porque es un promise y se tiene que esperar a que se resuelva
    if (response === 'USEREXISTS') {
      alert('El usuario ya existe');
    }
    else {
      alert('Usuario creado');
    }
    window.location.reload();
  }
  )
}

function checkUser(mail, pass, trainer = false) {
  return new Promise((resolve, reject) => { // Se tiene que usar promise porque fetch es asincrono
    let data = {
      email: mail,
      password: pass,
    };
    let route = '';
    
    if (trainer) {
      route = 'http://localhost:5001/trainers';
    } else {
      route = 'http://localhost:5001/users';
    }
    
    fetch(route, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Acess-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      },
    })
      .then(response => response.json())
      .then(data => {
        let user = data.find(user => user.email === mail);
        console.log(user);

        if (user === undefined) {
          alert("El usuario no existe");
        }
        else if (user.password === pass) {
          console.log('Usuario logeado');
          resolve(true); // Resuelve la promesa
        } else {
          console.log('Usuario o contraseña incorrectos')
          resolve(false); // Resuelve la promesa
        }
      })
      .catch(error => {
        reject(error); // Para manejar errores
      });
  });
}



export const Form = () => {

  const handleRegisterUser = () => {
    if (document.getElementById('option_usuario').checked) {
      let email = document.getElementById('email').value;
      let password = document.getElementById('password').value;
      createUser(email, password);
    } else if (document.getElementById('option_trainer').checked) {
      alert('Solo se pueden registrar usuarios');
    } else {
      alert('Seleccione una opcion');
    }
  };

  const handleLogin = async () => { // Se tiene que especificar que es async para poder resolver las promesas
    if (!document.getElementById('option_usuario').checked && !document.getElementById('option_trainer').checked) {
      alert('Seleccione una opcion');
    } 
    else {
      let login_valido = false;
      login_valido = await checkUser(document.getElementById('email').value, document.getElementById('password').value, document.getElementById('option_trainer').checked); // El await es para esperar a que se resuelva la promesa
      if(login_valido && !document.getElementById('option_trainer').checked){
        localStorage.setItem('email', document.getElementById('email').value);
        window.location.href = "http://localhost:3000/user";
      }
      else if(login_valido && document.getElementById('option_trainer').checked){
        localStorage.setItem('email', document.getElementById('email').value);
        window.location.href = "http://localhost:3000/trainer";
      }
      else{
        alert('Usuario o contraseña incorrectos');
      }
    }
  };

  const [renderUserLogin, setRenderUserLogin] = useState(false);
  
  return (
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
  )
}

export default Form;