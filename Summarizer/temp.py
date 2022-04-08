import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('en_sum/distilbart-cnn-12-6')
model = torch.load('en_sum/distilbart-cnn-12-6/pytorch_model')

#model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")


#torch.save(model, 'pytorch_model')
long_text = 'The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'

inputs = tokenizer([long_text], return_tensors="pt")
summary_ids = model.generate(inputs["input_ids"])
print(tokenizer)
print(tokenizer.batch_decode(summary_ids, skip_special_tokens=True))

def summary(long_text: str) -> str:
    return model(long_text)

