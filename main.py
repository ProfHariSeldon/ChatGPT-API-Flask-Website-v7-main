# pip install Flask openai
# openai migrate

##with open("./static/chromosomes.py") as f:
##    exec(f.read())

from flask import Flask, request, render_template, redirect
import openai
# Import the os module to interact with operating system features.  This includes fetching environment variables.
import os
# Import specific classes or functions directly from their modules to avoid prefixing them with the module name.
# Import the OpenAI library
## import openai
from openai import OpenAI
from openai._utils._httpx_client import SyncHttpxClient
# from openai import OpenAI
# Import the load_dotenv and find_dotenv functions from the dotenv package.
# These are used for loading environment variables from a .env file.
from dotenv import load_dotenv, find_dotenv

# Load environment variables from a .env file.
_ = load_dotenv(find_dotenv())

# Set the OpenAI API key by retrieving it from the environment variables.
# OpenAI.api_key = os.environ['OPENAI_API_KEY']
# OpenAI.assistant_key = os.environ['ASSISTANT_ID']

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
        http_client=SyncHttpxClient()  # avoids proxy injection issue
)

# can be empty
## client = openai.OpenAI(
    # This is the default and can be omitted
    ## api_key = os.environ.get("OPENAI_API_KEY"),
    # assistant_id = os.environ.get('ASSISTANT_ID')/
## )

# https://stackoverflow.com/questions/78018805/how-to-execute-custom-actions-with-chatgpt-assistants-api
assistantId = os.environ.get('ASSISTANT_ID')

# https://www.youtube.com/watch?v=pZUDEQs89zc
# https://mer.vin/2023/11/chatgpt-assistants-api/
# https://platform.openai.com/docs/assistants/overview?context=with-streaming
import time

# Step 1: Create an Assistant
##assistant = client.beta.assistants.create(
##    name="Transcriptome Classifier",
##    instructions="I want you to act as a scientific data visualizer. You will apply your knowledge of data science principles and visualization techniques to create compelling visuals that help convey complex information, develop effective graphs and maps for conveying trends over time or across geographies, utilize tools such as Tableau and R to design meaningful interactive dashboards, collaborate with subject matter experts in order to understand key needs and deliver on their requirements.",
##    # model="gpt-4-1106-preview"
##    model="gpt-3.5-turbo"
##)

# Step 2: Create a Thread
thread = client.beta.threads.create()

# Step 3: Add a Message to a Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    ## content = "What information would you like about the transcriptome?",
    content = "How many circRNAs are in hsa_hg38_circRNA.bed?"
)

from typing_extensions import override
from openai import AssistantEventHandler
 
# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
 
class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)
      
    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)
      
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)
  
    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)

# Then, we use the `create_and_stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.
 
with client.beta.threads.runs.create_and_stream(
    thread_id=thread.id,
    assistant_id=assistantId,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
    event_handler=EventHandler(),
) as stream:
  stream.until_done()

# https://stackoverflow.com/questions/46698134/how-to-post-the-output-result-on-the-same-page-in-flask-app
# https://chat.openai.com/g/g-b2dsUQrfB-transcriptome-classifier/c/d770e3a5-f565-4b7b-a234-6a75e81aec0a
@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = ""
    response = ""
    graph = ""
    selected_graph = ""
    
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        selected_graph = request.form.get('graph')
        
        if prompt:
            try:
                # completion = openai.Completion.create(
                completion = client.chat.completions.create(
                    ## model='gpt-3.5-turbo',
                    model='gpt-4-turbo',
                    # assistant_id=assistantId,
                    messages=[{"role": "user", "content": prompt}]
                    # engine="text-davinci-003",
                    # engine="gpt-3.5-turbo",  # You can use other models like "gpt-3.5-turbo"
                    # prompt=prompt,
                    # temperature=0.7,
                    # max_tokens=150,
                    # top_p=1.0,
                    # frequency_penalty=0.0,
                    # presence_penalty=0.0
                )
                response = completion.choices[0].message.content
            except Exception as e:
                response = f"An error occurred: {str(e)}"

        if selected_graph:
            try:
                print("Selected Graph = ", selected_graph)
                    
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt

                files_paths = {
                    'genes': './static/hg38_genes.bed',
                    'introns': './static/hg38_introns.bed',
                    'CDS': './static/hg38_CDS.bed',
                    '5p': './static/hg38_5p.bed',
                    '3p': './static/hg38_3p.bed',
                    'circRNA': './static/hsa_hg38_circRNA.bed',
                    'exons' : './static/hg38_exons.bed'
                }
                bed_dfs = {}

                for key, path in files_paths.items():
                    bed_dfs[key] = pd.read_csv(path, sep='\t', header=None)

                def adjust_frequency_for_chromosome(df, chromosome, bins):
                    df_chr = df[df[0] == chromosome]
                    positions = df_chr[1]._append(df_chr[2])
                    freq, bin_edges = np.histogram(positions, bins=bins)
                    return freq, bin_edges
                    
                chromosome = selected_graph
                bins = 100
                frequencies = {}
                bin_edges_dict = {}
                for key, df in bed_dfs.items():
                    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

                plt.figure(figsize=(15, 10))
                for key, freq in frequencies.items():
                    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')
                
                chromosome_number = chromosome[3:]
                if chromosome_number == 'MT':
                    chromosome_number = 'ChrMitochondria'
                    plt.xlabel(f'Genomic Position on Mitochondiral Chromosome')
                    plt.ylabel('Frequency')
                    plt.title(f'Frequency of Genomic Features on Mitochondiral Chromosome')
                    plt.legend()
                    plt.savefig(f'./static/images/{chromosome_number}.png')
                    plt.close()
                    graph = f'../static/images/{chromosome_number}.png'
                else:
                    plt.xlabel(f'Genomic Position on Chromosome {chromosome_number}')
                    plt.ylabel('Frequency')
                    plt.title(f'Frequency of Genomic Features on Chromosome {chromosome_number}')
                    plt.legend()
                    plt.savefig(f'./static/images/{chromosome_number}.png')
                    plt.close()
                    graph = f'../static/images/{chromosome_number}.png'
                    
                print("graph path = ", graph)
            except Exception as e:
                response = f"An error occurred: {str(e)}"
                
    return render_template('index.html', prompt=prompt, response=response, graph=graph)

if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='8080', port=5000)
    # server.run(debug=True, host='0.0.0.0', port=5000)

# https://stackoverflow.com/questions/78018805/how-to-execute-custom-actions-with-chatgpt-assistants-api
# https://platform.openai.com/docs/api-reference/models/delete
# https://www.youtube.com/watch?v=pZUDEQs89zc
# https://platform.openai.com/docs/assistants/overview?context=with-streaming
