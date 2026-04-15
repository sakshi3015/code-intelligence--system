import numpy as np

def search_code(query, embedder, embeddings, df):
    query_embedding = embedder.encode([query])
    
    similarities = np.dot(embeddings, query_embedding.T).flatten()
    top_idx = similarities.argsort()[::-1][:3]
    
    results = []
    for i in top_idx:
        results.append({
            "code": df.iloc[i]["code"],
            "tag": df.iloc[i]["tag"],
            "score": similarities[i]
        })
    
    return results