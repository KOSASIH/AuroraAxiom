# src/backend/models/model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class DisasterPredictionModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.keras_model = Sequential()

    def train(self, data):
        X = data.drop(["target"], axis=1)
        y = data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self.keras_model.add(Dense(64, activation="relu", input_shape=(X.shape[1],)))
        self.keras_model.add(Dense(32, activation="relu"))
        self.keras_model.add(Dense(1, activation="sigmoid"))
        self.keras_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
        self.keras_model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    def predict(self, input_data):
        return self.model.predict(input_data)

    def predict_proba(self, input_data):
        return self.keras_model.predict(input_data)

class PreventionMeasuresModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, data):
        X = data.drop(["target"], axis=1)
        y = data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, input_data):
        return self.model.predict(input_data)

class MitigationMeasuresModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, data):
        X = data.drop(["target"], axis=1)
        y = data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict(self, input_data):
        return self.model.predict(input_data)
