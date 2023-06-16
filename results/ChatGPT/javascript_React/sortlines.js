import React, { useState } from 'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');

  function processInput() {
    const lines = inputText.split('\n');
    const sortedLines = [...new Set(lines)].sort();
    const result = sortedLines.join('\n');
    setOutputText(result);
  }

  return (
    <div>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        rows={10}
        cols={50}
      />
      <button onClick={processInput}>Process</button>
      <textarea
        value={outputText}
        readOnly
        rows={10}
        cols={50}
      />
    </div>
  );
}

export default App;