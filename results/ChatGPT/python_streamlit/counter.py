import streamlit as st

# Set initial value of counter
counter = 1

# Define function to increase counter
def increase_counter():
    global counter
    counter += 1

# Define function to decrease counter
def decrease_counter():
    global counter
    if counter > 1:
        counter -= 1

# Define function to reset counter
def reset_counter():
    global counter
    counter = 1

# Create Streamlit app
st.title("Counter App")

# Display counter
st.header(f"Counter: {counter}")

# Create buttons
col1, col2, col3 = st.beta_columns(3)
with col1:
    if st.button("Increase"):
        increase_counter()
with col2:
    if st.button("Decrease"):
        decrease_counter()
with col3:
    if st.button("Reset"):
        reset_counter()