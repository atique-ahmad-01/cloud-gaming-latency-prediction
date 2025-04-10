import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(data_path):
    df = pd.read_csv(data_path)
    df.dropna(inplace=True)

    label_encoders = {}
    for col in ['user_id', 'asn_org', 'server_name']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df[['user_id', 'longitude', 'latitude', 'asn_org', 'server_name', 'latency_min', 'latency_max', 'jitter']]
    y = df['latency_avg']
    
    return X, y, label_encoders
