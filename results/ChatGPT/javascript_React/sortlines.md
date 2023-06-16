Here's an example of how you could implement this React application:

```jsx
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
```

In this code, we use the `useState` hook to keep track of the input and output text. The `processInput` function is called when the button is clicked, and it splits the input text into lines using the `\n` character as a delimiter. We then use the `Set` object to remove any duplicates, and the spread operator (`...`) to convert the resulting set back into an array. Finally, we sort the lines alphabetically and join them back together with the `\n` character to create the output text.

The two textareas are rendered using the `value` prop for the input and output text, and the `onChange` prop to update the input text when the user types in the textarea. The second textarea is marked as `readOnly` so that the user can't edit the output text directly.

Overall, this should give you a basic idea of how to build a simple React application that processes text input. You could add more features to this app, such as the ability to save and load text files, or to filter out certain lines based on a search term.