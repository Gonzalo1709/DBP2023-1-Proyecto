import React, { useEffect } from 'react'

export const Trainer = () => {

  // get the selected date from local storage

  // Selected date is a number. Format it so that it is "YYYY-MM-DD"
  // YYYY is current year, MM is current month, DD is selected date with leading 0 if necessary
  let currentMonth = new Date().toLocaleString('en-US', { month: 'long' });
  let email_de_entrenador = localStorage.getItem('email');


  const getSessions = async () => {
    let id_de_entrenador = localStorage.getItem('trainerID');
    let current_date = localStorage.getItem('selectedDate');
    if (current_date < 10) {
      current_date = `0${current_date}`;
    }
    // format month to where it has leading 0 if necessary
    if (new Date().getMonth() + 1 < 10) {
      current_date = `${new Date().getFullYear()}-0${new Date().getMonth() + 1}-${current_date}`;
    }
    else {
      current_date = `${new Date().getFullYear()}-${new Date().getMonth() + 1}-${current_date}`;
    }

      let route = `https://zergixz.pythonanywhere.com/sessions/${id_de_entrenador}/${current_date}`;
      console.log(route);
      const response = await fetch(route, {
          method: 'GET',
          headers: {
              'Content-Type': 'application/json',
              'Acess-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          },
      });
      let data = await response.json();
      let amount = data.length;
      console.log(amount);
      localStorage.setItem('amount', amount);
      return data;
  }





  const handleClick = async (event) => {
    console.log(event.target.dataset.day);
    localStorage.setItem('selectedDate', event.target.dataset.day);
    let trainerID = await getTrainerIdByEmail(localStorage.getItem("email"));
    localStorage.setItem('trainerID', trainerID);
    let daySessions = await getSessions(`${event.target.dataset.day}-${new Date().getMonth() + 1}-${new Date().getFullYear()}`);
    // convert daySessions to JSON
    daySessions = JSON.stringify(daySessions);
    localStorage.setItem('daySessions', daySessions);
    window.location.href = "http://localhost:3000/trainer_day_sessions";
  };

  currentMonth = new Date().toLocaleString('en-US', { month: 'long' });

  const getTrainerIdByEmail = async (email) => {
    let route = `https://zergixz.pythonanywhere.com/trainers`;
    let response = await fetch(route, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Acess-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      },
    });
    let data = await response.json();
    let trainer = data.find(trainer => trainer.email === email);
    return trainer.id;
  };

  

  const checkIfDateHasSessions = async (date) => {
    let sessions = await getSessions(date);
    if (sessions.length === 0) {
      return false;
    } else {
      return true;
    }
  };

  const makeArrayOfDaysWithSessions = async () => {
    // make a binary array of days with sessions. 1 if it has sessions, 0 if it doesn't
    let daysInMonth = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0).getDate();
    let daysArr = [];

    for (let i = 1; i <= daysInMonth; i++) {
      // eslint-disable-next-line
      const current_date = `${i}-${new Date().getMonth() + 1}-${new Date().getFullYear()}`;
      let sesionesEnElDia = false;
      sesionesEnElDia = await checkIfDateHasSessions(current_date);
      if (sesionesEnElDia) {
        daysArr.push(1);
      }
      else {
        daysArr.push(0);
      }
    }
    localStorage.setItem('daysArr', daysArr);
    
    return daysArr;
  };

  const renderDaysOfMonth = () => {
    const daysInMonth = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0).getDate();
    const days = [];
    const daysArr = localStorage.getItem('daysArr');

    for (let i = 1; i <= daysInMonth; i++) {
      // eslint-disable-next-line
      const current_date = `${i}-${new Date().getMonth() + 1}-${new Date().getFullYear()}`;
      // check index i-1 of daysArr to see if it has sessions. If it does, set li style "color: red"
      if (daysArr[i-1] === 1) {
        days.push(<li key={i} data-day={i} onClick={handleClick} style={{color: "red"}}>{i}</li>);
      }
      else {
        days.push(<li key={i} data-day={i} onClick={(handleClick)}>{i}</li>);
      }
    }
    return days;
  };

  let loading = localStorage.getItem('loading');
  loading = loading === 'true';
  
  useEffect(() => {
    if (loading) {
      (async () => {
      await makeArrayOfDaysWithSessions();
      console.log("days rendered")
      loading = false;
      localStorage.setItem('loading', loading);
      window.location.reload();
      })();
    }

  }, []);


    
  console.log(loading);
  if (loading) {
    
    // return a loading screen which will load the days and periodically check if they have been loaded
    // when they are loaded, it will render the calendar
    return (
      <div>
        <div id="body2">
          <div id="form-body2">
            <p id="text2">Bienvenido Entrenador {email_de_entrenador} </p>
          </div>
          <div className="Loading">
            <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" alt="loading" />
          </div>
        </div>
      </div>
    );
  } else {
    console.log("rendering calendar");
    return (
      <div>
        <div id="body2">
          <div id="form-body2">
            <p id="text2">Bienvenido Entrenador {email_de_entrenador} </p>
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
  }
};


export default Trainer;