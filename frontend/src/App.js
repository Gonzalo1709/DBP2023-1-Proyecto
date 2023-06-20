import React from 'react';
import {Routes, Route } from 'react-router-dom';
import DefaultPage from './components/DefaultPage';
import Trainer from './components/trainer';
import User from './components/user';
import TableUser from './components/table_user';

function App() {
  return (
    <div>
    <Routes>
        <Route path="/user" element={<User />}>
        </Route>
        <Route path="/trainer" element={<Trainer />}>
        </Route>
        <Route path="/" element={<DefaultPage/>}>
        </Route>
        <Route path="/table" element={<TableUser/>}>
        </Route>
    </Routes>
    </div>
  );
}


export default App;
