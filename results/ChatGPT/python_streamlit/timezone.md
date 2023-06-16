As an AI language model, I cannot create a Streamlit application. However, I can provide you with the code that you can use to create a Streamlit application that displays a Time Zone dropdown list and shows the current time in the selected time zone.

Here is the code:

```
import streamlit as st
from datetime import datetime
import pytz

# Create a list of time zones
time_zones = pytz.all_timezones

# Create a dropdown list for time zones
selected_time_zone = st.selectbox("Select a time zone", time_zones)

# Get the current time in the selected time zone
current_time = datetime.now(pytz.timezone(selected_time_zone))

# Display the current time in the selected time zone
st.write(f"The current time in {selected_time_zone} is {current_time}")
```

In this code, we first import the necessary libraries - Streamlit, datetime, and pytz. We then create a list of all time zones using the `pytz.all_timezones` function.

Next, we create a dropdown list using the `st.selectbox` function and pass in the list of time zones as the options. The user can select a time zone from this dropdown list.

We then get the current time in the selected time zone using the `datetime.now` function and passing in the selected time zone as an argument.

Finally, we display the current time in the selected time zone using the `st.write` function.

You can save this code in a Python file and run it using the command `streamlit run <filename>.py`. This will start a Streamlit server and open the application in your web browser.