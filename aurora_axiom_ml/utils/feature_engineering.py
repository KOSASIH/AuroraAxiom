import pandas as pd
from sklearn.preprocessing import StandardScaler

def extract_features(data):
    features = pd.DataFrame()
    features['latitude'] = data['latitude']
    features['longitude'] = data['longitude']
    features['timestamp'] = pd.to_datetime(data['timestamp']).dt.hour
    features['category'] = pd.get_dummies(data['category']).values
    return features

def scale_features(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features
