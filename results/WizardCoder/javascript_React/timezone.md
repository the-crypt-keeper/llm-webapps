```javascript
import React, { useState } from "react";

function App() {
  const [timeZone, setTimeZone] = useState("UTC");
  const [currentTime, setCurrentTime] = useState(new Date());

  const handleTimeZoneChange = (event) => {
    setTimeZone(event.target.value);
  };

  const handleTimeUpdate = () => {
    setCurrentTime(new Date());
  };

  return (
    <div>
      <h1>Time Zone Converter</h1>
      <div>
        <label htmlFor="timeZone">Time Zone:</label>
        <select id="timeZone" value={timeZone} onChange={handleTimeZoneChange}>
          <option value="UTC">UTC</option>
          <option value="America/New_York">Eastern Time (US & Canada)</option>
          <option value="Asia/Tokyo">Japan</option>
          <option value="Europe/London">British Time (UK)</option>
        </select>
      </div>
      <div>
        <label htmlFor="currentTime">Current Time:</label>
        <input
          id="currentTime"
          type="text"
          value={currentTime.toLocaleTimeString()}
          readOnly
        />
      </div>
      <button onClick={handleTimeUpdate}>Update Time</button>
    </div>
  );
}

export default App;
```