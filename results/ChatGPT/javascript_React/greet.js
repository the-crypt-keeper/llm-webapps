import React, { useState } from 'react';

const Greeting = () => {
  const [name, setName] = useState('');
  const [language, setLanguage] = useState('English');
  const [greeting, setGreeting] = useState('');

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleLanguageChange = (event) => {
    setLanguage(event.target.value);
  };

  const handleGreetClick = () => {
    switch (language) {
      case 'English':
        setGreeting(`Hello ${name}!`);
        break;
      case 'French':
        setGreeting(`Bonjour ${name}!`);
        break;
      case 'Spanish':
        setGreeting(`Hola ${name}!`);
        break;
      default:
        setGreeting('');
    }
  };

  return (
    <div>
      <label htmlFor="name">Name:</label>
      <input type="text" id="name" value={name} onChange={handleNameChange} />
      <br />
      <label htmlFor="language">Language:</label>
      <select id="language" value={language} onChange={handleLanguageChange}>
        <option value="English">English</option>
        <option value="French">French</option>
        <option value="Spanish">Spanish</option>
      </select>
      <br />
      <button onClick={handleGreetClick}>Greet</button>
      <br />
      <p>{greeting}</p>
    </div>
  );
};

export default Greeting;