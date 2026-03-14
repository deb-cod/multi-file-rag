from fastapi import FastAPI
from retrieval.retriever import retrieve
from llm.generator import generate_answer

app = FastAPI()


@app.get("/ask")
def ask(query: str):

    docs = retrieve(query)

    context = "\n".join(docs)

    answer = generate_answer(context, query)

    return {
        "question": query,
        "answer": answer,
        "sources": docs
    }