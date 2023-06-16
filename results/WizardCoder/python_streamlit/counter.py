import streamlit as st

# Set initial value of counter
counter = 1

# Display counter
st.write("Counter:", counter)

# Define functions to handle button clicks
def increase():
    global counter
    counter += 1
    st.write("Counter:", counter)

def decrease():
    global counter
    if counter > 1:
        counter -= 1
        st.write("Counter:", counter)

def reset():
    global counter
    counter = 1
    st.write("Counter:", counter)

# Display buttons
st.button("Increase", on_click=increase)
st.button("Decrease", on_click=decrease)
st.button("Reset", on_click=reset)