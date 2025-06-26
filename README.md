# ChatGPT-API-Flask-Website-v7-main

## Details of how I wrote the webpage:</h2>
https://chatgpt-api-flask-website-v7-main.onrender.com/

1\. To chat with ChatGPT 4 I copied python code from GitHub and modified it and added my own HTML code.  Details follow:

1A. There are 14 lines copied from GitHub https://github.com/redemptionwxy/ChatGPT-API-Flask-Website to create the ChatGPT 4 text box one can ask any question of then push the submit button.  I copied and improved two lines to run the app and host it on port 5000 no longer port 80.</ul>

1B. In index.html, my 22 lines of HTML code creates the Submit button

2. To dynamically generate the graphs, I queried ChatGPT and it gave me most of the python code without the import modules.  I added code to import the necessary library modules.   I consolidated the ChatGPT dynamic graphing code to fewer lines.  And I wrote HTML code for the radio buttons.  Details follow:</p>

2A. I created ./static/chromosmoes.py to generate the graphs in 716 lines I modified from ChatGPT.  I looked up how to add radio buttons to select which graph you want to dynamically generate and implemented that.  I consolidated the ChatGPT graph generating code to be much shorter (18 lines in main.py of which graph was chosen from the radio button) and put it in main.py and no longer use ./static/chromosmoes.py 716 lines.  I copied and improved one line to return render_template('index.html', prompt=prompt, response=response, graph=graph) which is to send the variables prompt, response, and graph to index.html, to make the webpage dynamic, that I got from ChatGPT but added graph=graph.

2B. In index.html, 56 lines are my radio buttons I wrote after looking up how to make radio buttons from documentation and 8 lines with the if and endif I wrote after looking up how to do ifs in HTML.  1 line is the submit button from GitHub https://github.com/redemptionwxy/ChatGPT-API-Flask-Website

3\. One feature I tried to program for this webpage did not work out and I omitted it from the webpage.  I was unable to get ChatGPT to answer questions about my graphs using my Transcriptome Classifier CustomGPT, because it had parameters to answer pregenerated questions in the terminal (while building the webpage) but no parameters to answer questions outside of the terminal in GET and POST in the text box that I used to ask ChatGPT 4 for help but could not replace that with my Transcriptome Classifier CustomGPT.

3A. I figured out how to add the ChatGPT 4 api_key and assistantID. There are 30 lines I copied from the ChatGPT documentation https://platform.openai.com/docs/assistants/overview?context=with-streaming to ask questions in the terminal.

4. Then I started getting a 402 error because the hosting service broke, so I updated openai==1.14.3 to openai==1.92.0 in requirements.txt and used ChatGPT and https://platform.openai.com/docs/api-reference/runs/createRun?lang=python to update to modern OpenAI API calls.  The documentation said that Custom GPTs like my <a href="Transcriptome Classifier">https://chatgpt.com/g/g-b2dsUQrfB-transcriptome-classifier?model=gpt-4o</a> are "currently only accessible via the ChatGPT interface (web or app) and not through the API." so I could not add that <a href="Transcriptome Classifier">https://chatgpt.com/g/g-b2dsUQrfB-transcriptome-classifier?model=gpt-4o</a> to this webpage and the assistants are only a way to send text to a ChatGPT before the end user does, for example telling ChatGPT to act like a bioinformatics scientist.  That was not deemed important for this webpage so I did not do it.


Code for this webpage is on my GitHub: https://github.com/ProfHariSeldon/ChatGPT-API-Flask-Website-v7-main

Thomas H. Lipscomb
