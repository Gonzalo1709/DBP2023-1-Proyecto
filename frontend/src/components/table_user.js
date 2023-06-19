import React from 'react'
import "/Users/sergioherrerajave/proyectdbp2023/DBP2023-1-Proyecto/frontend/src/components/table_user.css"

export const TableUser = () => {
  return (
    <div id = "body-table">
    <table id="table-user">
        <tbody>
            <tr>
                <td id='table-td'>Fecha</td>
                <td id='table-td'><input id="table-input" type= "datetime-local"></input></td>
            </tr>
            <tr>
                <td id='table-td'>Duración</td>
                <td id='table-td'><input id="table-input" type= "time"></input></td>
            </tr>
            <tr>
                <td id='table-td'>Tipo</td>
                <td id='table-td'><input id="table-input" type= ""></input></td>
            </tr>
            <tr>
                <td id='table-td'>Entrenador</td>
                <td id='table-td'><input id="table-input" type= ""></input></td>
            </tr>
            <tr>
                <td id='table-td'>Precio</td>
                <td id='table-td'><input id="table-input" type= "number"></input></td>
            </tr>
            <tr>
                <td id='table-td' colspan="2"><input id="table-input" type="submit" value="Submit"></input></td>
            </tr>
        </tbody>
    </table>
    </div>
  )
}

export default TableUser;