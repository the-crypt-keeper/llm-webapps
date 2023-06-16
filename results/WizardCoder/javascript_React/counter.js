import React, { useState } from'react';

function Counter() {
  const [count, setCount] = useState(1);

  const handleIncrease = () => {
    setCount(count + 1);
  };

  const handleDecrease = () => {
    if (count > 1) {
      setCount(count - 1);
    }
  };

  const handleReset = () => {
    setCount(1);
  };

  return (
    <div>
      <h1>{count}</h1>
      <div>
        <button onClick={handleIncrease}>Increase</button>
        <button onClick={handleDecrease}>Decrease</button>
        <button onClick={handleReset}>Reset</button>
      </div>
    </div>
  );
}

export default Counter;