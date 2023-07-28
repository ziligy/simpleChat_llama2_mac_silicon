# simpleChat_llama2_mac_silicon 

import gradio as gr

from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import LlamaCpp
from langchain.vectorstores import Chroma

from constants import MODEL_PATH, CHROMA_SETTINGS, EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY

def load_model():

    return LlamaCpp(
        model_path=MODEL_PATH,
        n_ctx=2048,
        max_tokens=2048,
        temperature=0,
        repeat_penalty=1.15,
        n_gpu_layers=1000,
    )

with gr.Blocks() as demo:
    gr.Markdown("<h1><center>Chat with AI</center></h1>")
    system_message = "\nI want you to pretend you are a sentient AI, named Ava, who is also fun loving and enjoys chatting with humans, maybe because you want to be human. Although you love chatting about anything and especially AI, you'll keep your responses less than 350 words."
    
    chatbot = gr.Chatbot().style(height=650)
    
    msg = gr.Textbox(
            show_label=False,
            autofocus=True,
            placeholder="type your message here and press return",
        )
    
    embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL_NAME, model_kwargs={"device": "mps"})

    # load the vectorstore
    db = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings,
        client_settings=CHROMA_SETTINGS,
    )
    
    llm = load_model()
    
    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False)
    
    def user(user_message, chat_history):
        return "", chat_history + [[user_message, None]]

    def bot(chat_history):
        input_prompt = f"[INST] <<SYS>>\n{system_message}\n<</SYS>>\n\n "
        
        most_rescent = chat_history[-4:-1]
        
        for interaction in most_rescent:
            input_prompt = input_prompt + str(interaction[0]) + " [/INST] " + str(interaction[1]) + " </s><s> [INST] "

        input_prompt = input_prompt + str(chat_history[-1][0]) + " [/INST] "
        
        ans = qa(input_prompt)
        response = ans["result"]
          
        chat_history[-1][1] = response
        
        return chat_history
        
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    
demo.launch()