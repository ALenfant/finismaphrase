import os
import random

from transformers import AutoTokenizer, TFAutoModelForSequenceClassification, pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.nlp = None

    def initialize(self):
        """
        Initializes everything, takes a bit of time
        """
        cache_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "storage", "hfcache")

        # Load pretrained model and tokenizer
        model = TFAutoModelForSequenceClassification.from_pretrained("tblard/tf-allocine", cache_dir=cache_path)
        tokenizer = AutoTokenizer.from_pretrained("tblard/tf-allocine", cache_dir=cache_path)

        self.nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

    def classify(self, text):
        return self.nlp(text)

    def is_negative(self, text):
        classification = self.classify(text)
        assert len(classification) == 1
        return classification[0]["label"] == "NEGATIVE"


if __name__ == "__main__":
    print("Init")
    sa = SentimentAnalyzer()
    print("OK")
    sa.initialize()
    print("OK2")
    text = "C'est d'la merde ta magie"
    print(sa.classify(text), sa.is_negative(text))
    text = "Trop cool! Merci"
    print(sa.classify(text), sa.is_negative(text))
