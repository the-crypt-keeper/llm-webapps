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