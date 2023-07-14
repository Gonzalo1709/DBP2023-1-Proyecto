import React from "react";
import './App.css'

export const TableTrainer = () => {

    const email_de_entrenador = localStorage.getItem('email');
    const load_sessions = JSON.parse(localStorage.getItem('daySessions'));

    const constructTableElements = () => {
        let cant_iter = localStorage.getItem("amount");
        const tableElements = [];
        for (let i = 0; i < cant_iter; i++) {
            console.log("i")
            tableElements.push(
                <tr key={i}>
                    <td>{load_sessions[i]["fecha"]}</td>
                    <td>{load_sessions[i]["precio"]}</td>
                    <td>{load_sessions[i]["usuario_id"]}</td>
                </tr>
            );
        }
        console.log(tableElements);
        return tableElements;
    };

    const handleClick = async (event) => {
        localStorage.removeItem('selectedDate');
        localStorage.removeItem('daySessions');
        window.location.href = "http://localhost:3000/trainer";
    };



    return (
        <div>
            <div id="body2">
                <div id="form-body2">
                    <p id="text2">Bienvenido Entrenador {email_de_entrenador} </p>
                </div>
                <div className="Sesiones">
                    <div className="month">
                        <ul>
                            <li>Sesiones</li>
                        </ul>
                    </div>
                    <table id='days'>
                        <thead id="CabeceraTablaVertical">
                            <tr id="Cabecilla">
                                <th id="backgrounded">Fecha</th>
                                <th id="backgrounded">Precio</th>
                                <th id="backgrounded">Usuario</th>
                            </tr>

                            </thead>
                        <tbody id = "ColumnaDetabla">
                            {constructTableElements()}
                        </tbody>
                        
                </table>
                <button id="boton" onClick={handleClick}>Volver</button>
        </div>
    </div>
        </div>
    );
};

export default TableTrainer;