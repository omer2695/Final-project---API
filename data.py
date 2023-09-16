import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    df = pd.read_csv('dataset.csv', encoding="ISO-8859-1")
    return df

def preprocess_data(df):
    # Perform data preprocessing here (e.g., label encoding)
    le_storage = LabelEncoder()
    le_Public_Transport = LabelEncoder()
    le_Public_parking = LabelEncoder()

    df['storage_n'] = le_storage.fit_transform(df['storage'])
    df['Public_Transport_n'] = le_Public_Transport.fit_transform(df['Public Transport'])
    df['Public_parking_n'] = le_Public_parking.fit_transform(df['Public parking'])

    return df
