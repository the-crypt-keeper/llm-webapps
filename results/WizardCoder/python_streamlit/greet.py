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