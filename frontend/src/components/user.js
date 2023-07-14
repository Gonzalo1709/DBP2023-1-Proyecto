import React from 'react';
import TableUser from './table_user';
import './table_user.css'

export const Userlogin = () => {
  const currentMonth = new Date().toLocaleString('en-US', { month: 'long' });
  const email_de_usuario = localStorage.getItem('email');

  const handleClick = (event) => {;
    localStorage.setItem('day', event.target.value);
    window.location.href = "http://localhost:3000/table_user";
  };

  const renderDaysOfMonth = () => {
    const daysInMonth = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0).getDate();
    const days = [];

    for (let i = 1; i <= daysInMonth; i++) {
      const current_date = `${i}-${new Date().getMonth() + 1}-${new Date().getFullYear()}`;
      days.push(<li key={i} value={i} onClick={handleClick}>{i}</li>);
    }

    return days;
  };

  return (
    <div>
      <div id="body2">
        <div id="form-body2">
          <p id="text2">Bienvenido Usuario {email_de_usuario} </p>
        </div>
        <div className="calendar">
          <div className="month">
            <ul>
              <li>{currentMonth}</li>
            </ul>
          </div>
          <ul className="weekdays">
            <li>Mo</li>
            <li>Tu</li>
            <li>We</li>
            <li>Th</li>
            <li>Fr</li>
            <li>Sa</li>
            <li>Su</li>
          </ul>
          <ul className="days">{renderDaysOfMonth()}</ul>
        </div>
      </div>
    </div>
  );
};

export default Userlogin;
