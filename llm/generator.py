import os
from llama_cpp import Llama

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "Meta-Llama-3-8B-Instruct.Q4_K_M.gguf")

llm = Llama(model_path=MODEL_PATH, n_ctx=4096)


def generate_answer(context, query):

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    output = llm(prompt, max_tokens=300)

    return output["choices"][0]["text"]