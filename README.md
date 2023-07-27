# simpleChat_llama2_mac_silicon
A simple chat example exclusively for local execution on mac/apple silicon. 

This repo is a distillation and riff based off [privateGPT](https://github.com/imartinez/privateGPT) and [localGPT](https://github.com/PromtEngineer/localGPT) which I created to exclusively run locally on Apple Silicon and more specificly my MacBook Pro (M1). My motivation was to create minimum viable LLM chat for my device, for learning purposes.

## Features
- uses [llama.cpp](https://github.com/ggerganov/llama.cpp) via [LangChain](https://python.langchain.com/docs/get_started/introduction.html) framework
- Models from [Hugging Face](https://huggingface.co)
- [Gradio](https://www.gradio.app) UI




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

*Gradio*

```shell
conda install -c conda-forge gradio
```

*Metal acceleration* ([reference](https://developer.apple.com/metal/pytorch/))

```shell
conda install pytorch torchvision torchaudio -c pytorch-nightly
```

*upgrade llama-cpp-python for Metal*

```shell
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir
```

*requirements.txt*

```shell
pip install -r requirements.txt
```

## Starting the Gradio Server

```shell
gradio app.py
```

You should see:
*Running on local URL:  http://127.0.0.1:7861*

cmd + click on the link to start the UI in your browser


## Instructions for ingesting your own dataset

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