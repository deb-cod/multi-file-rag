from sentence_transformers import SentenceTransformer

def get_embedding_model():
    """
    :return:
    returns a sentence embedding matrix
    """
    model = SentenceTransformer("BAAI/bge-small-en")
    return model