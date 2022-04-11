FROM continuumio/miniconda3:latest
RUN conda update --all -y && \
    conda install -c conda-forge transformers langdetect nltk pika && \
    conda clean -ay

WORKDIR /home/summarizer
COPY . .

RUN python model_importer.py

CMD ["server.py"]
ENTRYPOINT ["python"]