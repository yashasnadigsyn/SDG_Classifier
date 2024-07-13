import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer

with open("OneVsRest/SDG_classifier.pkl", "rb") as f:
    MODEL = pickle.load(f)

with open("OneVsRest/tfidf_vectorizer.pkl", "rb") as f:
    TF_IDF = pickle.load(f)

with open("OneVsRest/multilabel_binarizer.pkl", "rb") as f:
    MULTILABEL = pickle.load(f)

def predict_sdg(text_content):
    X = TF_IDF.transform([text_content])
    predictions = MODEL.predict(X)
    predicted_labels = MULTILABEL.inverse_transform(predictions)

    return predicted_labels
