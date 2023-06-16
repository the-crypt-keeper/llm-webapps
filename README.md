# LLM Webapp Experiments

How well can LLM create a simple webapp? Let's find out.

# Tasks

<TODO>

- timezone
- greet
- counter
- sortlines

# Running

`generate.py`

NOTE: The starchat gradio that the generations is aimed at it is down right now.

# Results

`streamlit run app.py` to open the result browser

## Notes

### WizardCoder
- Without `Please return only the full, complete source code for the application in a single code block.` in the prompt, WizardCoder sometimes answers in a step-by-step style with the final result at the end.  This is both difficult to parse and a huge waste of tokens/time.