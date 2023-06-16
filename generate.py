import yaml
import time
import re
import os
from jinja2 import Template

def run_chatgpt(prompt):
    from langchain.chat_models import ChatOpenAI
    from langchain import LLMChain, PromptTemplate

    chatgpt_params = { 'temperature': 0.7, 'max_tokens': 1024, 'top_p': 0.1, 'presence_penalty': 1.17 }
    model = ChatOpenAI(model_name='gpt-3.5-turbo', **chatgpt_params)
    chain = LLMChain(llm=model, prompt=PromptTemplate(template='{input}', input_variables=['input']))
    answer = chain.run(input=prompt)

    return answer 

def run_wizardcoder(prompt):
    from gradio_client import Client

    client = Client('https://8821d10c477083e9.gradio.app/')
    wizardcoder_params = { 'temperature': 1.0, 'beams': 1, 'max_tokens': 1024, 'top_k': 40, 'top_p': 1.0 }
    job = client.submit(
			prompt,
			wizardcoder_params['temperature'], # temperature
			wizardcoder_params['top_p'], # top_p
			wizardcoder_params['top_k'],  # top_k
            wizardcoder_params['beams'], # beams
			wizardcoder_params['max_tokens'], # max_tokens
			fn_index=0
    )
    while not job.done():
        time.sleep(5)
        print(job.status())

    return job.outputs()[-1]

# Useful functions for extracting code from LLM responces
def extract_code_markdown(answer):
    # Look for start tokens   
    match = re.search(r'```(\w*)', answer)
    start_token = match.group(0) if match else None
    start_index = match.start() if match else -1

    # If we didn't find a start token, return None
    if start_index == -1:
        return None

    # Find the index of the end token, starting from the end of the start token.
    # if not found, assume we're taking the whole thing.
    end_token = "```"
    end_index = answer.find(end_token, start_index + len(start_token) + 1)
    if end_index == -1:
        end_index = len(answer)

    # Extract the text between the tokens
    code_text = answer[start_index + len(start_token):end_index].strip()

    return code_text

# Expand input yaml to create a list of tasks
def expand_inputs(filename):
    projects = yaml.safe_load(open(filename))
    inputs = []

    for template in projects['Templates'].keys():
        for vars in projects['Variables']:
            for prj in projects['Projects']:
                prompt = Template(prj['Prompt']).render(**vars)
                model_input = Template(projects['Templates'][template]).render(prompt=prompt, **vars)
                inputs.append({ 'project': prj['Name'], 'model': template, 'input': model_input, **vars })

    return inputs

output_template = "results/{{model}}/{{language}}_{{library}}"
extensions = { 'HTML': 'html', 'python': 'py', 'javascript': 'js' }

# When called as a CLI, execute the tasks.
if __name__ == "__main__":
    for task in expand_inputs('projects.yaml'):
        print(task['input'])

        if task['model'] == 'ChatGPT':            
            task['output'] = run_chatgpt(task['input'])
        elif task['model'] == 'WizardCoder':
            task['output'] = run_wizardcoder(task['input'])

        task['code'] = extract_code_markdown(task['output'])
        if task['code'] is None:
            task['code'] = task['output']
        
        outdir = Template(output_template).render(**task)
        os.makedirs(outdir, exist_ok=True)

        with open(f"{outdir}/{task['project']}.txt", 'w') as f:
            f.write(task['input'])

        with open(f"{outdir}/{task['project']}.md", 'w') as f:
            f.write(task['output'])
        
        with open(f"{outdir}/{task['project']}.{extensions[task['language']]}", 'w') as f:
            f.write(task['code'])

        print(f"Generated {outdir}/{task['project']}")