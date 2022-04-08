from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('en_sum/distilbart-cnn-12-6')
model = AutoModelForSeq2SeqLM.from_pretrained("en_sum/distilbart-cnn-12-6")


def summary(long_text: str) -> str:
    inputs = tokenizer([long_text], return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"])
    return tokenizer.batch_decode(summary_ids, skip_special_tokens=True)


