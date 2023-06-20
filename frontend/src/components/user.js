import React from 'react'
import TableUser from './table_user';

export const Userlogin = () => {
  const currentMonth = new Date().toLocaleString('en-US', { month: 'long' });

  const renderDaysOfMonth = () => {
    const daysInMonth = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0).getDate();
    const days = [];
  
    for (let i = 1; i <= daysInMonth; i++) {
      days.push(<li key={i}>{i}</li>);
    }
  
    return days;
  };

  return (
    <div>
      <TableUser />
        <div id="body2">
        <div id="form-body2">
          <p id="text2">Bienvenido usuario</p>
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
          <ul className="days">
            {renderDaysOfMonth()}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Userlogin;