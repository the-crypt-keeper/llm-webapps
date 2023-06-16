import streamlit as st

# Define a dictionary of greetings in different languages
greetings = {
    'English': 'Hello',
    'French': 'Bonjour',
    'Spanish': 'Hola'
}

# Create a dropdown selection box for language
language = st.selectbox('Select a language', ('English', 'French', 'Spanish'))

# Create a text input field for name
name = st.text_input('Enter your name')

# Create a button to greet the user
if st.button('Greet'):
    # Get the greeting based on the selected language
    greeting = greetings[language]
    # Display the greeting with the user's name
    st.write(f'{greeting}, {name}!')