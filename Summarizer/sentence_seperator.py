import nltk


def sep_sent(long_text: str, tokenizer) -> [str]:
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
    return chunks
