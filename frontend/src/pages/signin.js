import { useState } from 'react';
import axios from 'axios';

export default function Signin() {
  const [form, setForm] = useState({
    username: '',
    password: '',
    is_creator: false
  });
  const [message, setMessage] = useState('');

  const handleChange = e => {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSignup = async () => {
    try {
      await axios.post('http://localhost:8000/api/accounts/signup/', form);
      setMessage('Signup successful!');
    } catch (error) {
      setMessage('Signup failed!');
    }
  };

  const handleSignin = async () => {
    try {
      await axios.post('http://localhost:8000/api/accounts/signin/', form);
      setMessage('Signin successful!');
    } catch (error) {
      setMessage('Signin failed!');
    }
  };

  return (
    <div>
      <h1>Sign In / Sign Up</h1>
      <input
        name="username"
        placeholder="Username"
        value={form.username}
        onChange={handleChange}
      />
      <input
        name="password"
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={handleChange}
      />
      <label>
        Creator:
        <input
          type="checkbox"
          name="is_creator"
          checked={form.is_creator}
          onChange={handleChange}
        />
      </label>
      <div>
        <button onClick={handleSignup}>Sign Up</button>
        <button onClick={handleSignin}>Sign In</button>
      </div>
      {message && <p>{message}</p>}
    </div>
  );
}
