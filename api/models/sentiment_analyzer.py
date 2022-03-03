import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')


class SentimentModel:

    def __init__(self, sentence):
        self.sentence = sentence
        self.processed_sentence = self.preprocess()
        self.polarity = self.calculate_polarity()
        self.compound = self.calculate_compound()

    def preprocess(self):
        stop_words = stopwords.words('english')
        stemmatizer = PorterStemmer()

        self.sentence = self.sentence.lower()
        tokens = word_tokenize(self.sentence)
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [stemmatizer.stem(w) for w in tokens]
        
        return " ".join(tokens)

    def calculate_polarity(self):
        return TextBlob(self.processed_sentence).sentiment.polarity

    def calculate_compound(self):
        return SentimentIntensityAnalyzer().polarity_scores(self.processed_sentence)['compound']




