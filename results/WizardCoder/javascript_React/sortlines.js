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