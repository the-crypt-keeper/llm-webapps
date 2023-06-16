# LLM Webapp Experiments

How well can LLM create a simple webapp? Let's find out.

# Tasks

- timezone
- greet
- counter
- sortlines

## Notes

### WizardCoder
- Without `Please return only the full, complete source code for the application in a single code block.` in the prompt, WizardCoder sometimes answers in a step-by-step style with the final result at the end.  This is both difficult to parse and a huge waste of tokens/time.