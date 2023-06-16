```python
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
```

Explanation:

- We first import the `streamlit` library.
- We set the initial value of the counter to 1.
- We display the counter using the `st.write()` function.
- We define three functions to handle button clicks: `increase()`, `decrease()` and `reset()`.
- The `increase()` function adds 1 to the counter and updates the display.
- The `decrease()` function subtracts 1 from the counter if it is greater than 1, and updates the display.
- The `reset()` function sets the counter back to 1 and updates the display.
- We display the three buttons using the `st.button()` function, passing in the button label and the corresponding function to handle the button click.