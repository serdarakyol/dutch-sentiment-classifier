from os.path import dirname, abspath

from sentiment_classification_api.models.model_sentiment_classify import SentimentClassifyRequest, SentimentClassifyResponse
from sentiment_classification_api.utils.utils import CleanText, load_json, load_vectorizer, load_model

from scipy.sparse import hstack

ROOT_DIR = dirname(dirname(abspath(__file__)))

# Load model
model = load_model(ROOT_DIR + "/data/ComplementNB_sentiment_classify.model")
# Load stopwords
stopwords = load_json(ROOT_DIR + "/data/stopwords_nl.json")
# Load vectorizers
word_vectorizer = load_vectorizer(ROOT_DIR + "/data/clean_word_vectorizer.pkl")
char_vectorizer = load_vectorizer(ROOT_DIR + "/data/clean_char_vectorizer.pkl")


class SentimentClassify:
    def classify(self, content_request: SentimentClassifyRequest) -> SentimentClassifyResponse:
        id2label = {
            1: 'neutral',
            2: 'positive',
            0: 'negative'
        }
        content = content_request.content

        # clean text
        cleaner = CleanText(stopwords)
        clean_content = cleaner.clean_content(content)
        
        # extract features
        word_transformed = word_vectorizer.transform([clean_content])
        char_transformed = char_vectorizer.transform([clean_content])
        
        # stack features
        stacked_features = hstack([word_transformed, char_transformed])

        # prediction
        classify_result = model.predict(stacked_features)
        result = {
            "content": content,
            "sentiment": id2label[classify_result[0]]
        }

        return result
