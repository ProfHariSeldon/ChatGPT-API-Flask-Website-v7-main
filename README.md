# ChatGPT-API-Flask-Website-v7-main

## Details of how I wrote the webpage:</h2>
https://chatgpt-api-flask-website-v7-main.onrender.com/

1\. To chat with ChatGPT 4 I copied python code from GitHub and modified it and added my own HTML code.  Details follow:

1A. There are 14 lines copied from GitHub https://github.com/redemptionwxy/ChatGPT-API-Flask-Website to create the ChatGPT 4 text box one can ask any question of then push the submit button.  I copied and improved two lines to run the app and host it on port 5000 no longer port 80.</ul>

1B. In index.html, my 22 lines of HTML code creates the Submit button

2\. To dynamically generate the graphs, I queried ChatGPT and it gave me most of the python code without the import modules.  I added code to import the necessary library modules.   I consolidated the ChatGPT dynamic graphing code to fewer lines.  And I wrote HTML code for the radio buttons.  Details follow:</p>

2A. I created ./static/chromosmoes.py to generate the graphs in 716 lines I modified from ChatGPT.  I looked up how to add radio buttons to select which graph you want to dynamically generate and implemented that.  I consolidated the ChatGPT graph generating code to be much shorter (18 lines in main.py of which graph was chosen from the radio button) and put it in main.py and no longer use ./static/chromosmoes.py 716 lines.  I copied and improved one line to return render_template('index.html', prompt=prompt, response=response, graph=graph) which is to send the variables prompt, response, and graph to index.html, to make the webpage dynamic, that I got from ChatGPT but added graph=graph.

2B. In index.html, 56 lines are my radio buttons I wrote after looking up how to make radio buttons from documentation and 8 lines with the if and endif I wrote after looking up how to do ifs in HTML.  1 line is the submit button from GitHub https://github.com/redemptionwxy/ChatGPT-API-Flask-Website

3\. One feature I tried to program for this webpage did not work out and I omitted it from the webpage.  I was unable to get ChatGPT to answer questions about my graphs using my Transcriptome Classifier CustomGPT, because it had parameters to answer pregenerated questions in the terminal (while building the webpage) but no parameters to answer questions outside of the terminal in GET and POST in the text box that I used to ask ChatGPT 4 for help but could not replace that with my Transcriptome Classifier CustomGPT.

3A. I figured out how to add the ChatGPT 4 api_key and ChatGPT Transcriptome Classifier Custom GPT assistantId. There are 30 lines I copied from the ChatGPT documentation https://platform.openai.com/docs/assistants/overview?context=with-streaming to ask questions in the terminal.  The terminal question, while building the webpage, is set here: content = "How many circRNAs are in hsa_hg38_circRNA.bed?".  The answer the terminal gives is 183718 circRNAs and is correct.  However, the terminal documentation https://platform.openai.com/docs/assistants/overview?context=with-streaming does not explain how to ask that terminal question in a webpage, because thread = client.beta.threads.create() and message = client.beta.threads.messages.create() both seem to not have the parameters to be in a webpage only in terminal parameters.  I asked for help from the ChatGPT help desk and they said they needed help from a collegue and they would get back to me.  That is all of the code before @app.route('/', methods=['GET', 'POST']) in main.py.

Code for this webpage is on my GitHub: https://github.com/ProfHariSeldon/ChatGPT-API-Flask-Website-v7-main

Thomas H. Lipscomb
