```python
import streamlit as st

# Define the list of languages
languages = ["English", "French", "Spanish"]

# Define the function to greet the user in the selected language
def greet_user(name, language):
    if language == "English":
        return f"Hello {name}!"
    elif language == "French":
        return f"Bonjour {name}!"
    elif language == "Spanish":
        return f"¡Hola {name}!"
    else:
        return "Invalid language selected."

# Display the drop-down selection box and text entry field
language = st.selectbox("Select a language:", languages)
name = st.text_input("Enter your name:")

# Display the greet button and the greeting message when clicked
if st.button("Greet"):
    greeting = greet_user(name, language)
    st.write(greeting)
```

Explanation:

- We first import the `streamlit` library which is used to build the web application.
- We define a list of languages that we want to display in the drop-down selection box.
- We define a function `greet_user` that takes in the user's name and the selected language and returns a greeting message in the selected language.
- We display the drop-down selection box and the text entry field using the `st.selectbox` and `st.text_input` functions respectively.
- We display the greet button using the `st.button` function.
- When the greet button is clicked, we call the `greet_user` function with the user's name and selected language and store the greeting message in a variable called `greeting`.
- We display the greeting message using the `st.write` function.