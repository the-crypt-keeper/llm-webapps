```python
import streamlit as st

def process_text(text):
    lines = text.split('\n')
    lines = sorted(set(lines))
    return '\n'.join(lines)

st.title('Text Processor')

input_text = st.text_area('Enter text here')

if st.button('Process'):
    output_text = process_text(input_text)
    st.text_area('Output', output_text, height=200)
```

Explanation:

- We import the `streamlit` library which is used to build the web application.
- We define a function `process_text` which takes in the input text and returns the processed text.
- We create a `title` for the web application.
- We create a `text_area` for the user to enter the input text.
- We create a `button` for the user to click to process the input text.
- When the user clicks the button, we call the `process_text` function with the input text and store the output in a variable `output_text`.
- We create another `text_area` for the user to see the output text. We set the `height` parameter to 200 to make the output area scrollable.