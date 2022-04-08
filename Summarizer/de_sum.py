from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("deutsche-telekom/mt5-small-sum-de-mit-v1")

model = AutoModelForSeq2SeqLM.from_pretrained("deutsche-telekom/mt5-small-sum-de-mit-v1")

print(tokenizer)