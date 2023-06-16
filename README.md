# LLM Webapp Experiments

How well can LLM create a simple webapp? Let's find out.

# Results

[See Results On HuggingFace Spaces](https://huggingface.co/spaces/mike-ravkine/llm-webapps-results)

`streamlit run app.py` to open the result browser


# Tasks

## greet

Greet the user in their native language.

## timezone

What time is it in different timezones? A simple task in terms of UX but tricky processing to get right.

## counter

An up/down counter with reset.

## sortlines

A simple data processing application.

# Running

`generate.py`

## Notes

### WizardCoder
- Without `Please return only the full, complete source code for the application in a single code block.` in the prompt, WizardCoder sometimes answers in a step-by-step style with the final result at the end.  This is both difficult to parse and a huge waste of tokens/time.