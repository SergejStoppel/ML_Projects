#!/bin/sh

python model_importer.py

git lfs install
export GIT_LFS_SKIP_SMUDGE=1

PWD=$(pwd)

SUMMARY_DIR="$PWD/models"

SUMMARY_DIR_EN="$SUMMARY_DIR"/en_sum
SUMMARY_MODEL_DIR_EN="$SUMMARY_DIR_EN"/distilbart-cnn-12-6
MODEL_URL_EN=https://huggingface.co/sshleifer/distilbart-cnn-12-6

if [ ! -d "$SUMMARY_MODEL_DIR_EN" ]; then  
    mkdir -p "$SUMMARY_DIR_EN" && cd "$SUMMARY_DIR_EN"
    git clone "$MODEL_URL_EN" "$SUMMARY_MODEL_DIR_EN"
fi

cd "$SUMMARY_MODEL_DIR_EN" && git lfs pull --include "pytorch_model.bin"

SUMMARY_DIR_DE="$SUMMARY_DIR"/de_sum
SUMMARY_MODEL_DIR_DE="$SUMMARY_DIR_DE"/bert2bert_shared-german-finetuned-summarization
MODEL_URL_DE=https://huggingface.co/mrm8488/bert2bert_shared-german-finetuned-summarization

if [ ! -d "$SUMMARY_MODEL_DIR_DE" ]; then  
    mkdir -p "$SUMMARY_DIR_DE" && cd "$SUMMARY_DIR_DE"
    git clone "$MODEL_URL_DE" "$SUMMARY_MODEL_DIR_DE"
fi

cd "$SUMMARY_MODEL_DIR_DE" && git lfs pull --include "pytorch_model.bin"

SUMMARY_DIR_MULTI="$SUMMARY_DIR"/multi_sum
SUMMARY_MODEL_DIR_MULTI="$SUMMARY_DIR_MULTI"/mT5_multilingual_XLSum
MODEL_URL_MULTI=https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum

if [ ! -d "$SUMMARY_MODEL_DIR_MULTI" ]; then  
    mkdir -p "$SUMMARY_DIR_MULTI" && cd "$SUMMARY_DIR_MULTI"
    git clone "$MODEL_URL_MULTI" "$SUMMARY_MODEL_DIR_MULTI"
fi

cd "$SUMMARY_MODEL_DIR_MULTI" && git lfs pull --include "pytorch_model.bin"

SUMMARY_DIR_NL="$SUMMARY_DIR"/nl_sum
SUMMARY_MODEL_DIR_NL="$SUMMARY_DIR_NL"/t5-v1.1-base-dutch-cnn-test
MODEL_URL_NL=https://huggingface.co/yhavinga/t5-v1.1-base-dutch-cnn-test

if [ ! -d "$SUMMARY_MODEL_DIR_NL" ]; then  
    mkdir -p "$SUMMARY_DIR_NL" && cd "$SUMMARY_DIR_NL"
    git clone "$MODEL_URL_NL" "$SUMMARY_MODEL_DIR_NL"
fi

cd "$SUMMARY_MODEL_DIR_NL" && git lfs pull --include "pytorch_model.bin"