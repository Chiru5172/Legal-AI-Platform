from embedding_model import get_embedding_model

emb = get_embedding_model()
vector = emb.embed_query("Breach of contract due to delayed payment")

print("Vector length:", len(vector))
print(vector[:10])
