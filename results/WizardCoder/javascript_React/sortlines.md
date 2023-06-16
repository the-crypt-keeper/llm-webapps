```javascript
import React, { useState } from'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleProcessClick = () => {
    const lines = inputText.split('\n');
    const uniqueLines = [...new Set(lines)];
    const sortedLines = uniqueLines.sort();
    setOutputText(sortedLines.join('\n'));
  };

  return (
    <div>
      <textarea value={inputText} onChange={handleInputChange} />
      <button onClick={handleProcessClick}>Process</button>
      <textarea value={outputText} readOnly />
    </div>
  );
}

export default App;
```

This is a basic implementation of the application. It uses the `useState` hook to manage the input and output text areas. The `handleInputChange` function is called whenever the user types in the input area. The `handleProcessClick` function is called when the user clicks the 'Process' button. It splits the input text into lines, removes duplicates using the `Set` object, sorts the remaining lines, and sets the output text to the sorted, de-duplicated lines. Finally, it renders the input and output areas and a 'Process' button.