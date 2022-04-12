FROM continuumio/miniconda3:latest
RUN conda update --all -y && \
    conda install -c conda-forge transformers langdetect nltk pika protobuf sentencepiece git-lfs && \
    conda clean -ay

WORKDIR /home/summarizer

COPY . .
RUN chmod +x models_populate.sh
RUN ./models_populate.sh

CMD ["server.py"]
ENTRYPOINT ["python"]