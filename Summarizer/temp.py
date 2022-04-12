import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('models/en_sum/distilbart-cnn-12-6')
model = torch.load('en_sum/distilbart-cnn-12-6/pytorch_model.bin')

#model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
#model.save_pretrained('de_sum/bert2bert_shared-german-finetuned-summarization')
model.save_pretrained('multi_sum/mT5_multilingual_XLSum')
tokenizer.save_pretrained('multi_sum/mT5_multilingual_XLSum')

#torch.save(model, 'pytorch_model.bin')


