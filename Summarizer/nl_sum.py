from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sentence_seperator

tokenizer = AutoTokenizer.from_pretrained('models/nl_sum/t5-v1.1-base-dutch-cnn-test')
model = AutoModelForSeq2SeqLM.from_pretrained('models/nl_sum/t5-v1.1-base-dutch-cnn-test')


def summary(long_text: str) -> str:
    if len(long_text) > tokenizer.model_max_length:
        chunks = sentence_seperator.sep_sent(long_text, tokenizer)
        inputs = [tokenizer(c, return_tensors='pt') for c in chunks]
        for input in inputs:
            outs = model.generate(**input)
        return ''.join(tokenizer.batch_decode(*outs, skip_special_tokens=True))
    else:
        inputs = tokenizer([long_text], return_tensors='pt')
        outs = model.generate(inputs['input_ids'])
        return tokenizer.batch_decode(outs, skip_special_tokens=True)




