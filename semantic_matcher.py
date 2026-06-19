from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = None

def load_model():

    global model

    if model is None:

        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return model


def semantic_match(
    resume_text,
    jd_text
):

    model = load_model()

    resume_embedding = model.encode(
        resume_text
    )

    jd_embedding = model.encode(
        jd_text
    )

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(
        similarity * 100,
        2
    )