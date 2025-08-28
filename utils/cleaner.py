import string

class Cleaner:
    """

    """
    def __init__(self, _processed_str : str):
        self.processed_str = _processed_str

    def clean(self):
        """
        Apply all the clean options, to one func.
        :return: str
        """
        self.lower_str()
        self.remove_punctuation()
        self.remove_special_symbols()
        self.remove_white_space()
        self.remove_stop_words()
        self.lemmatization_text()


        return self.processed_str


    def lower_str(self):
        self.processed_str = self.processed_str.lower()
        return

    def remove_punctuation(self):
        translator = str.maketrans("", "", string.punctuation)
        self.processed_str = self.processed_str.translate(translator)
        return


    def remove_special_symbols(self):
        import re
        self.processed_str = re.sub(r'\W+', ' ', self.processed_str)
        return

    def remove_white_space(self):

        self.processed_str = self.processed_str.replace("\n", " ").replace("\r", ' ').replace("\t", " ")
        self.processed_str = " ".join(self.processed_str.split())

        return

    def remove_stop_words(self):
        import nltk
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize

        nltk.download('stopwords')
        nltk.download('punkt_tab')

        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(self.processed_str.lower())
        self.processed_str = ' '.join([word for word in tokens if word not in stop_words])

        return

    def lemmatization_text(self):
        from nltk.tokenize import word_tokenize
        from nltk.stem import WordNetLemmatizer
        import nltk

        nltk.download('punkt_tab')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger_eng')

        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(self.processed_str)
        self.processed_str = ' '.join([lemmatizer.lemmatize(word) for word in tokens])


        return
