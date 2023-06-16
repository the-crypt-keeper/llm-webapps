```python
import streamlit as st
import pytz
import datetime

# Create a list of time zones
time_zones = pytz.common_timezones

# Create a dropdown list to select time zone
selected_time_zone = st.selectbox("Select Time Zone", time_zones)

# Get the current time in the selected time zone
current_time = datetime.datetime.now(pytz.timezone(selected_time_zone))

# Display the current time in the selected time zone
st.write("Current Time in", selected_time_zone, ":", current_time.strftime("%Y-%m-%d %H:%M:%S"))
```

Explanation:

- We first import the necessary libraries - `streamlit`, `pytz`, and `datetime`.
- We create a list of time zones using the `common_timezones` attribute of the `pytz` module.
- We create a dropdown list using the `st.selectbox()` function, which takes two arguments - the label for the dropdown list and the list of options.
- We get the current time in the selected time zone using the `datetime.datetime.now()` function and passing the selected time zone as an argument.
- We display the current time in the selected time zone using the `st.write()` function, which takes the label and the value to display.