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