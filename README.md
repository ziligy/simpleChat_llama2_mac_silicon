# simpleChat_llama2_mac_silicon
A simple chat app with embeddings and vector database, exclusively for local execution on mac/apple silicon. 

This repo is a distillation and riff based off [privateGPT](https://github.com/imartinez/privateGPT) and [localGPT](https://github.com/PromtEngineer/localGPT) which I created to exclusively run locally on Apple Silicon and more specificly my MacBook Pro (M1). My motivation was to create minimum viable LLM chat running completly local on my device, for learning purposes.

<img src="https://github.com/ziligy/simpleChat_llama2_mac_silicon/blob/main/example/example_chat_screen.png" alt="SimpleChat by ziligy" height="535" align="left">

## Features
- LlamaCpp from [llama.cpp](https://github.com/ggerganov/llama.cpp)
- Models from [Hugging Face](https://huggingface.co)
- Embeddings from [Hugging Face](https://huggingface.co)
- Vector Database from [Chroma](https://www.trychroma.com)
- LangChain Framework [LangChain](https://python.langchain.com/docs/get_started/introduction.html)
- UI via [Gradio](https://www.gradio.app)

## Requirements
- [Mac computer with Apple silicon](https://support.apple.com/en-us/HT211814)
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) 

## Create & activate New Conda environment

```shell
conda create -n simpleChat python=3.11
conda activate simpleChat
```

## Clone the Repo

```shell
git clone https://github.com/ziligy/simpleChat_llama2_mac_silicon simpleChat
cd simpleChat
```

## Installation

*LangChain*
```shell
conda install -c conda-forge langchain 
```

*upgrade llama-cpp-python for Metal*

```shell
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir
```

*requirements.txt*

```shell
pip install -r requirements.txt
```

## Download GGML Model & Set MODEL_PATH

Download this model or another 4-bit(preferred) GGML (required) model

[llama-2-13b-chat.ggmlv3.q4_1.bin](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/blob/main/llama-2-13b-chat.ggmlv3.q4_1.bin)

***Define MODEL_PATH in *constants.py* to set the location and name of the model you are using.***

(e.g in *constants.py*) MODEL_PATH = os.path.expanduser( '~' ) + "/Models/llama-2-13b-chat.ggmlv3.q4_1.bin"


## Starting the Chat on Gradio Server

```shell
gradio app.py
```

You should see:
*Running on local URL:  http://127.0.0.1:7861*

cmd + click on the link to start the Chat UI in your browser

Go to your browser to chat with the AI.

***Note chat responses may take one to two minutes, so you'll need to be patient***

___

## Instructions for optionally ingesting your own dataset

*NOTE:* The ingest.py component is basicly a fork from [localGPT](https://github.com/PromtEngineer/localGPT) 

Put any and all of your .txt, .pdf, or .csv files into the SOURCE_DOCUMENTS directory

The current default file types are .txt, .pdf, .csv, and .xlsx, if you want to use any other file type, you will need to convert it to one of the default file types.

Run the following command to ingest all the data.

```shell
python ingest.py
```

It will create an index containing the local vectorstore. Will take time, depending on the size of your documents. 

If you want to start from an empty database, delete the DB folder. 

```shell
rm -r ./DB
```

Executing the *ingest.py* program will recreate a fresh DB directory 
