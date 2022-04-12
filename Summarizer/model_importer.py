import nltk
from transformers import AutoTokenizer

nltk.download('punkt')

# Get and save tokenizer for multi language model
tokenizer = AutoTokenizer.from_pretrained('models/multi_sum/mT5_multilingual_XLSum')
tokenizer.save_pretrained('models/multi_sum/mT5_multilingual_XLSum')
