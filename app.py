import streamlit as st
import streamlit.components.v1 as components

import os
import sys
import glob
import html

# Parse command-line arguments.
if len(sys.argv) > 1:
    folder = os.path.abspath(sys.argv[1])
else:
    folder = os.path.abspath(os.getcwd())

models = {x.replace(folder+'/results/',''): {} for x in glob.glob(folder+'/results/**')}
for model in models.keys():
    models[model] = {x.replace(f"{folder}/results/{model}/",''): [] for x in glob.glob(f"{folder}/results/{model}/**")}
    for env in models[model].keys():
        models[model][env] = [x.replace(f"{folder}/results/{model}/{env}/",'').replace('.txt','') for x in glob.glob(f"{folder}/results/{model}/{env}/*.txt")]

st.sidebar.header('LLM Webapp Experiments')
selected_model = st.sidebar.selectbox('Select a model', models.keys())
selected_env = st.sidebar.selectbox('Select an environment', models[selected_model].keys())
selected_project = st.sidebar.selectbox('Select a project', models[selected_model][selected_env])

fname_to_run = f'./results/{selected_model}/{selected_env}/{selected_project}.txt'
try:
    with open(fname_to_run) as f:
        prompt = f.read()
        st.sidebar.subheader('Prompt')
        st.sidebar.code(prompt)
except:
    st.sidebar.error('Error loading prompt.')

extensions = { 'HTML_jQuery': 'html', 'python_streamlit': 'py', 'javascript_React': 'js' }
fname_to_run = f'./results/{selected_model}/{selected_env}/{selected_project}.{extensions[selected_env]}'
try:
    with open(fname_to_run) as f:
        filebody = f.read()
except:
    st.error('Error loading file.')

if selected_env == 'python_streamlit':
    compiled_code = compile(filebody, filename=fname_to_run, mode='exec')
    exec(compiled_code, {})
    st.code(filebody)
elif selected_env == 'HTML_jQuery':
    components.html(filebody, height=400, scrolling=True)
    st.code(filebody)
else:
    hacked_js = '\n'.join([x for x in filebody.split('\n') if not 'export default' in x and not 'import' in x])
    #entrypoint = function App() {
    react_template = f"""
    <body>
        <div id="root"></div>
       
        <script src="https://unpkg.com/react@17/umd/react.development.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

        <script type="text/babel" data-presets="es2015, react">
          /**@jsx React.createElement */
          const {{ useState }} = React;
          {hacked_js}

          ReactDOM.render(<App />, document.getElementById('root'));
        </script>
    </body>
    """
    components.html(react_template, height=400, scrolling=True)
    st.code(filebody)