import logging

from generator import Generator
from sentiment_analyzer import SentimentAnalyzer


class SentenceCompleter():
    def __init__(self):
        self.generator = Generator()
        self.sentiment_analyzer = SentimentAnalyzer()

        # Initialize everything (takes time)
        self.generator.initialize()
        self.sentiment_analyzer.initialize()

    def complete_sentence(self, prefix):
        iteration = 0
        while iteration < 20:
            sentence = self.generator.complete(prefix)
            logging.info("Generated %s, trial %d" % (sentence, iteration))
            if not self.sentiment_analyzer.is_negative(sentence):
                return sentence
            logging.warning("Negative sentence generated: %s, trial %d" % (sentence, iteration))
            iteration += 1  # Try again

    def complete_prettify_shorten_sentence(self, prefix, length):
        sentence = self.complete_sentence(prefix)
        sentence = sentence.replace("' ", "'")[:length]
        if "." in sentence:
            sentence = sentence[:sentence.rfind(".") + 1]
        return sentence


if __name__ == "__main__":
    sentence_completer = SentenceCompleter()
    print(sentence_completer.complete_prettify_shorten_sentence("Haha salut", 280))
