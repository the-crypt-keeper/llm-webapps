import React, { useState } from'react';

function App() {
  const [language, setLanguage] = useState('English');
  const [name, setName] = useState('');

  const handleLanguageChange = (event) => {
    setLanguage(event.target.value);
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Hello ${name}, nice to meet you in ${language}!`);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Language:
          <select value={language} onChange={handleLanguageChange}>
            <option value="English">English</option>
            <option value="French">French</option>
            <option value="Spanish">Spanish</option>
          </select>
        </label>
        <br />
        <label>
          Name:
          <input type="text" value={name} onChange={handleNameChange} />
        </label>
        <br />
        <button type="submit">Greet</button>
      </form>
    </div>
  );
}

export default App;