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