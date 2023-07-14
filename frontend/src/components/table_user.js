import React from 'react'
import "./table_user.css"

const handleSubmit = (event) => {
    // query the id of the user based on the email
    let email = localStorage.getItem('email');
    fetch(`https://zergixz.pythonanywhere.com/users?email=${email}`)
    .then(response => response.json())
    .then(data1 => {
        localStorage.setItem('user_id', data1[0].id);
    })
    .catch(error => console.log(error));
    event.preventDefault();
    // const fecha = document.getElementById("fecha").value;
    let entrenador_id1 = 696969;
    let usuario_id1 = localStorage.getItem('user_id');
    usuario_id1 = parseInt(usuario_id1);
    let fecha1 = new Date();
    let loadDay = localStorage.getItem('day');
    let hora = "10:00:00";
    fecha1 = new Date(`${fecha1.getFullYear()}-${(fecha1.getMonth() + 1).toString().padStart(2, '0')}-${loadDay.toString().padStart(2, '0')} ${hora}`);
    let precio1 = 50;
    let data = [{entrenador_id:entrenador_id1, usuario_id:usuario_id1, fecha:fecha1, precio:precio1}];    
    console.log(data);
    let JSONdata = JSON.stringify(data);
    let test_data = [{
        "entrenador_id": 1,
        "usuario_id": 2,
        "fecha": "2023-07-04 10:00:00",
        "precio": 50
    }]
    let JSONTEST = JSON.stringify(test_data);
    // fix the date in JSONdata to have a format like this: 2021-05-01 10:00:00
    
    console.log(JSONdata);


    fetch('https://zergixz.pythonanywhere.com/sessions', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
        'Acess-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    },
        body: JSONTEST
    })
    window.location.href = "http://localhost:3000/user";
}

export const TableUser = () => {
  return (
    <div id = "body-table">
    <table id="table-user">
        <tbody>
            <tr>
                <td id='entrenador_id'>ID Entrenador</td>
                <td id='table-td'><input id="entrenador_id" type= ""></input></td>
            </tr>
            <tr>
                <td id='precio'>Precio S/.</td>
                <td id='table-td'><input id="precio" type= ""></input></td>
            </tr>
            <tr>
                <td id='hora'>Hora</td>
                <td id='table-td'><input id="hora" type= "time"></input></td>
            </tr>
            <tr>
                <td id='table-td' colspan="2"><input id="table-input" type="submit" value="Submit" onClick={handleSubmit}></input></td>
            </tr>
            
        </tbody>
    </table>
    </div>
  ) 
}

export default TableUser;