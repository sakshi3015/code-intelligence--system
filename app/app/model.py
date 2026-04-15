import os
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "dataset.csv")

df = pd.read_csv(file_path)

# Load model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = embedder.encode(df["code"].tolist())

def predict_tag(code):
    query_embedding = embedder.encode([code])
    
    import numpy as np
    similarities = np.dot(embeddings, query_embedding.T).flatten()
    
    best_match = similarities.argmax()
    return df.iloc[best_match]["tag"]

def get_data():
    return df, embeddings, embedder
