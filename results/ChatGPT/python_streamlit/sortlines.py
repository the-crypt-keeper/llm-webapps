import streamlit as st

def process_text(text):
    lines = text.split('\n')
    sorted_lines = sorted(set(lines))
    return '\n'.join(sorted_lines)

st.title("Text Processor")

input_text = st.text_area("Enter your text here", height=400)
if st.button("Process"):
    output_text = process_text(input_text)
    st.text_area("Processed Text", value=output_text, height=400)