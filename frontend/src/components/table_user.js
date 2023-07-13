import React from 'react'
import "./table_user.css"

const handleSubmit = (event) => {
    event.preventDefault();
    const fecha = document.getElementById("fecha").value;
    const duracion = document.getElementById("duracion").value;
    const tipo = document.getElementById("tipo").value;
    const entrenador = 1;
    const data = {entrenador, fecha, duracion, tipo};
    console.log(data);
    fetch('https://zergixz.pythonanywhere.com/sessions', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
    },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

export const TableUser = ({fecha}) => {
  return (
    <div id = "body-table">
    <table id="table-user">
        <tbody>
            <tr>
                <td id='table-td'>Fecha</td>
                <td id='fecha'><p>{fecha}</p></td>
            </tr>
            <tr>
                <td id='duracion'>Duración</td>
                <td id='table-td'><input id="table-input" type= "time"></input></td>
            </tr>
            <tr>
                <td id='tipo'>Tipo</td>
                <td id='table-td'><input id="table-input" type= ""></input></td>
            </tr>
            <tr>
                <td id='table-td' colspan="2"><input id="table-input" type="submit" value="Submit" onClick={handleSubmit}></input></td>
            </tr>
        </tbody>
    </table>
    </div>
  ) 
}

export default TableUser;