import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import datefinder


class Analysis:

    def __init__(self, text: str):
        self.text = text


    def define_sentiment(self):
            score = SentimentIntensityAnalyzer().polarity_scores(self.text)
            if score["compound"] >= 0.5:
                sentiment = "positive"
            elif score["compound"] >= -0.5:
                sentiment = "negative"
            else:
                sentiment = "neutral"

            return sentiment


    def weapons_detected(self, weapons: list):
        weapons_detected = []

        words = self.text.split()
        for word in words:
            if word in weapons:
                weapons_detected.append(word)

            if len(weapons_detected) == 0:
                weapons_detected = ""

            return weapons_detected


    def relevant_timestamp(self):
        relevant_timestamp = ""
        matches_timestamp = list(datefinder.find_dates(self.text))
        if len(matches_timestamp) > 0:
            last_timestamp = matches_timestamp[0]
            for timestamp in matches_timestamp:
                try:
                    print(timestamp)
                    if timestamp.year > last_timestamp.year:
                         last_timestamp = timestamp
                    elif timestamp.month > last_timestamp.month:
                        last_timestamp = timestamp
                    elif timestamp.day > last_timestamp.day:
                        last_timestamp = timestamp
                    else:
                        pass
                except Exception as e:
                    print(f"Error: {e}")
            relevant_timestamp = f"{last_timestamp.day}/{last_timestamp.month}/{last_timestamp.year}"
        return relevant_timestamp
