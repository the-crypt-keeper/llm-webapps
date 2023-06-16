Here's a sample code for the streamlit application that displays a drop-down selection box with the options English, French and Spanish, a text entry field captioned Name and the button "Greet". When the button is clicked, greet the user by name in the selected language.

```python
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
```

To run this code, save it as a Python file (e.g. `greeting_app.py`) and run the following command in your terminal:

```
streamlit run greeting_app.py
```

This will start a local server and open the app in your web browser. You can then select a language, enter your name and click the "Greet" button to see the greeting in the selected language.