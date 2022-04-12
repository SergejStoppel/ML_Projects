FROM continuumio/miniconda3:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    sudo && \
    apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN conda update --all -y && \
    conda install -c conda-forge transformers langdetect nltk pika protobuf sentencepiece git-lfs && \
    conda clean -ay
    
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
RUN groupadd --gid ${USER_GID} ${USERNAME} && \
    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} && \
    echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
SHELL [ "/bin/bash", "--login", "-c" ]
RUN conda init