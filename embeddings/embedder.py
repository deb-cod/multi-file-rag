from sentence_transformers import SentenceTransformer

def get_embedding_model(sentences):
    """
    :param sentences:
    takes a list of sentences and returns a sentence embedding matrix

    :return:
    returns a sentence embedding matrix
    """
    model = SentenceTransformer("BAAI/bge-small-en")
    return model