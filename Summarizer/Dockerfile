FROM continuumio/miniconda3:latest
RUN conda update --all -y && \
    conda install -c conda-forge transformers langdetect nltk && \
    conda clean -ay
WORKDIR /home/summarizer
COPY . .
#RUN chmod +x model_importer.py
RUN python model_importer.py
#CMD ['main.py']
#ENTRYPOINT ['/bin/bash', '-c']
