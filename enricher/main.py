import pandas as pd
from utils.cleaner import Cleaner
import string


processed_str="How to  remove  new line iii from string  in Python "
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords')
nltk.download('punkt_tab')
doc = "The researchers are developing advanced algorithms."

# Filter stopwords using spaCy
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(processed_str.lower())
filtered_tokens = [word for word in tokens if word not in stop_words]

print(filtered_tokens)





