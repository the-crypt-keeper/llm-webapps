```javascript
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
```

This is a basic React application that displays a drop-down selection box with the options English, French and Spanish, a text entry field captioned Name and the button "Greet". When the button is clicked, it greets the user by name in the selected language. The `useState` hook is used to manage the state of the language and name variables. The `handleLanguageChange`, `handleNameChange` and `handleSubmit` functions are used to handle the changes in the language and name fields, and the submission of the form. Finally, the `return` statement renders the form with the selected language and name fields, and the button to submit the form.