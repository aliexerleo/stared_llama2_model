# General description

This repo include packages python as: langchain ollama and streamlit. The application is a demo for running and test llama2 model. This app is componen for:

1- Amazon EC-2 (to runnig Ollama service).
2- Local environment (to runnig python script).

The python script make request to Ollama service. Ollama service by default listen in the port 11434. Yuo should be to specific this port.

# Langchain library.

Is a framework to integrations between LLMs and another python modules.

# Ollama

It is a service to run open source LLMs including llama2.

# Streamlit

Python Package to UI design. Focused in LLMs application

# Setting Up.

EC-2 INSTANCE:
1- Create EC-2 instance (8GB minimum requiriment).
2- Security group must have port 11434 open of anywhere source.
3- Install and running Ollama service (You can choose the open source model of your preference).

    command line:
    curl https://ollama.ai/install.sh | sh
    ollama run llama2

    IMPORTANT:
    You must be create the file of Ollama configuration. In this file Set Up two environment variables.
    OLLAMA_HOST and OLLAMA_ORIGINS

    mkdir -p /etc/systemd/system/ollama.service.d
    echo '[Service]' >>/etc/systemd/system/ollama.service.d/environment.conf

    echo 'Environment="OLLAMA_HOST=0.0.0.0:11434"' >>/etc/systemd/system/ollama.service.d/environment.conf

    echo 'Environment="OLLAMA_ORIGINS=http://192.168.1.1:*"' >>/etc/systemd/system/ollama.service.d/environment.conf

    systemctl daemon-reload
    systemctl restart ollama

    Now Ollama service is ready to allows request in port 11434.

LOCAL ENVIRONMENT (python script):

1- Install the file of requirements.
2- Run in local

    command line:
    pip install -r requirements.txt
    streamlit run app.py
    make any questio for the LLM model

# Resources and links

https://ollama.ai/download/linux
https://github.com/jmorganca/ollama/blob/main/docs/faq.md
https://docs.streamlit.io/library/api-reference/text/st.title
