```javascript
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
```

This is a basic implementation of a counter application with the functionality of increasing, decreasing and resetting the counter. The `useState` hook is used to manage the state of the counter. The `handleIncrease`, `handleDecrease` and `handleReset` functions are used to update the state of the counter based on the user's input. The `count` variable is used to display the current value of the counter. The `h1` tag is used to display the value of the counter. The `div` tag is used to group the buttons together. The `button` tags are used to display the buttons and the `onClick` attribute is used to bind the functions to the buttons. Finally, the `export default` statement is used to export the `Counter` component so that it can be used in other parts of the application.