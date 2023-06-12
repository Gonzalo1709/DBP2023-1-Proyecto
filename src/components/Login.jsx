import React, { useState } from 'react';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Perform login logic here, e.g. send login request to server

    // Reset form fields
    setEmail('');
    setPassword('');
  };

  return (
    <body>
    <div class="container">
      <button class="button" id="userButton">User</button>
      <button class="button">Trainer</button>
    </div>

    <script>
    document.getElementById('userButton').addEventListener('click', function() {
      window.location.href = 'login_usuario.html';
    });
    </script>
    </body>
  );
};

export default Login;
