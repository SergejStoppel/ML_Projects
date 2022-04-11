from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk

tokenizer = AutoTokenizer.from_pretrained('en_sum/distilbart-cnn-12-6')
model = AutoModelForSeq2SeqLM.from_pretrained('en_sum/distilbart-cnn-12-6')


def summary(long_text: str) -> str:
    if len(long_text) > tokenizer.model_max_length:
        sentences = nltk.tokenize.sent_tokenize(long_text)
        chunk = ''
        chunks = []
        length = 0
        count = -1
        for sentence in sentences:
            count += 1
            updated_length = len(tokenizer.tokenize(sentence)) + length
            if updated_length <= tokenizer.max_len_single_sentence:
                chunk += sentence + ' '
                length = updated_length
                if count == len(sentences) - 1:
                    chunks.append(chunk.strip())
            else:
                chunks.append(chunk.strip())
                chunk = ''
                # Taking care of the extra sentence
                chunk += sentence + ' '
                length = len(tokenizer.tokenize(sentence))
        inputs = [tokenizer(c, return_tensors='pt') for c in chunks]

        for input in inputs:
            outs = model.generate(**input)
        return ''.join(tokenizer.batch_decode(*outs, skip_special_tokens=True))
    else:
        inputs = tokenizer([long_text], return_tensors='pt')
        outs = model.generate(inputs['input_ids'])
        return tokenizer.batch_decode(outs, skip_special_tokens=True)




