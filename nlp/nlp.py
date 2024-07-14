import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

class AuroraAxiomNLP:
    def __init__(self):
        self.model = self.create_model()

    def create_model(self):
        df = pd.read_csv('nlp_data.csv')
        X = df['text']
        y = df['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        vectorizer = TfidfVectorizer(max_features=5000)
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)
        model = LogisticRegression(random_state=42)
        model.fit(X_train_tfidf, y_train)
        return model

    def predict(self, input_text):
        input_tfidf = vectorizer.transform([input_text])
        return model.predict(input_tfidf)

nlp = AuroraAxiomNLP()
