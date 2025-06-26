from flask import Flask, request, render_template
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from openai.http import HttpxBinaryClient  # Available in >=1.7.0
from openai.types.beta.threads import AssistantEventHandler  # ✅ FIXED IMPORT
from typing_extensions import override

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load environment variables
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ASSISTANT_ID = os.environ.get("ASSISTANT_ID")

# Flask app setup
app = Flask(__name__)

# OpenAI client with proxy-safe transport
client = OpenAI(
    api_key=OPENAI_API_KEY,
    http_client=HttpxBinaryClient()
)

# Event handler for streaming assistant response
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

# Thread + message + stream run
def start_assistant_thread():
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="How many circRNAs are in hsa_hg38_circRNA.bed?"
    )

    with client.beta.threads.runs.stream(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID,
        instructions="Please address the user as Jane Doe. The user has a premium account.",
        event_handler=EventHandler(),
    ):
        pass

# Run the assistant interaction on app start
start_assistant_thread()

# UI Route
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
                completion = client.chat.completions.create(
                    model='gpt-4-turbo',
                    messages=[{"role": "user", "content": prompt}]
                )
                response = completion.choices[0].message.content
            except Exception as e:
                response = f"An error occurred: {str(e)}"

        if selected_graph:
            try:
                print("Selected Graph =", selected_graph)
                files_paths = {
                    'genes': './static/hg38_genes.bed',
                    'introns': './static/hg38_introns.bed',
                    'CDS': './static/hg38_CDS.bed',
                    '5p': './static/hg38_5p.bed',
                    '3p': './static/hg38_3p.bed',
                    'circRNA': './static/hsa_hg38_circRNA.bed',
                    'exons': './static/hg38_exons.bed'
                }

                bed_dfs = {k: pd.read_csv(v, sep='\t', header=None) for k, v in files_paths.items()}

                def adjust_frequency_for_chromosome(df, chromosome, bins):
                    df_chr = df[df[0] == chromosome]
                    positions = pd.concat([df_chr[1], df_chr[2]])
                    freq, bin_edges = np.histogram(positions, bins=bins)
                    return freq, bin_edges

                bins = 100
                frequencies, bin_edges_dict = {}, {}
                for key, df in bed_dfs.items():
                    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, selected_graph, bins)

                plt.figure(figsize=(15, 10))
                for key, freq in frequencies.items():
                    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

                chromosome_number = selected_graph[3:]
                label = f'Chromosome {chromosome_number}' if chromosome_number != 'MT' else 'Mitochondrial Chromosome'
                img_name = 'ChrMitochondria' if chromosome_number == 'MT' else chromosome_number

                plt.xlabel(f'Genomic Position on {label}')
                plt.ylabel('Frequency')
                plt.title(f'Frequency of Genomic Features on {label}')
                plt.legend()
                image_path = f'./static/images/{img_name}.png'
                plt.savefig(image_path)
                plt.close()
                graph = f'../static/images/{img_name}.png'
                print("graph path =", graph)

            except Exception as e:
                response = f"An error occurred while generating the graph: {str(e)}"

    return render_template('index.html', prompt=prompt, response=response, graph=graph)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
