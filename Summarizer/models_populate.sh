#!/bin/sh

set -eu

git lfs install
export GIT_LFS_SKIP_SMUDGE=1

populate_lfs() {
    local MODEL_DIR=$1
    local MODEL_URL=$2
    local MODEL_INCLUDE=$3

    if [ ! -d "$MODEL_DIR" ]; then  
        git clone "$MODEL_URL" "$MODEL_DIR"
    fi

    git -C "$MODEL_DIR" lfs pull --include "$MODEL_INCLUDE"
}

WORKING_DIR=$(pwd)
MODELS_DIR="$WORKING_DIR"/models

SUMMARY_MODEL_DIR_EN="$MODELS_DIR"/en_sum/distilbart-cnn-12-6
MODEL_URL_EN=https://huggingface.co/sshleifer/distilbart-cnn-12-6

SUMMARY_MODEL_DIR_DE="$MODELS_DIR"/de_sum/bert2bert_shared-german-finetuned-summarization
MODEL_URL_DE=https://huggingface.co/mrm8488/bert2bert_shared-german-finetuned-summarization

SUMMARY_MODEL_DIR_MULTI="$MODELS_DIR"/multi_sum/mT5_multilingual_XLSum
MODEL_URL_MULTI=https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum

SUMMARY_MODEL_DIR_NL="$MODELS_DIR"/nl_sum/t5-v1.1-base-dutch-cnn-test
MODEL_URL_NL=https://huggingface.co/yhavinga/t5-v1.1-base-dutch-cnn-test

populate_lfs $SUMMARY_MODEL_DIR_EN $MODEL_URL_EN "pytorch_model.bin" &
populate_lfs $SUMMARY_MODEL_DIR_DE $MODEL_URL_DE "pytorch_model.bin" &
populate_lfs $SUMMARY_MODEL_DIR_MULTI $MODEL_URL_MULTI "pytorch_model.bin, spiece.model" &
populate_lfs $SUMMARY_MODEL_DIR_NL $MODEL_URL_NL "pytorch_model.bin" &

wait

python "$WORKING_DIR"/model_importer.py