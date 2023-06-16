import React, { useState } from 'react';

function App() {
  const [counter, setCounter] = useState(1);

  const increaseCounter = () => {
    setCounter(counter + 1);
  };

  const decreaseCounter = () => {
    if (counter > 1) {
      setCounter(counter - 1);
    }
  };

  const resetCounter = () => {
    setCounter(1);
  };

  return (
    <div>
      <h1>{counter}</h1>
      <div>
        <button onClick={increaseCounter}>Increase</button>
        <button onClick={decreaseCounter}>Decrease</button>
        <button onClick={resetCounter}>Reset</button>
      </div>
    </div>
  );
}

export default App;