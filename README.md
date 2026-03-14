# multi-file-rag




### To build docker image for Qdrant DB run:

- `INSTALL DOCKER IN YOUR COMPUTER`

Run this below command to build the image:

`docker build -t my-qdrant-db .`

Run this below command to run the container:

`docker run -d -p 6333:6333 -p 6334:6334 my-qdrant-db`


### To Load and save model in `model` directory:

Install Git LFS (Large File Storage)

- `git lfs install`

Run this to download the model, here: `Meta-Llama-3-8B-GGUF`

- `git clone https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF`

- This will create a folder Meta-Llama-3-8B-GGUF with multiple .gguf files (different quantizations like Q4, Q5, Q8)

- Pick the quantization you want (for local use, Q4_K_M is a good balance)


Copy the model into models
- `copy Meta-Llama-3-8B-GGUF\llama-3-8b.Q4_K_M.gguf models\`

### DOCUMENT: https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF

For NOW lets download **Q4_K_M** for a good balance: https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf

### FOR ANY ISSUE IN DOWNLOADING THE MODEL, REFER THE HUGGING FACE *DOCUMENT*


## To run the pipeline (watcher):
`python config.py`

## To run the FAST API:
`uvicorn api.main:app --reload`

### Open browser:
`http://127.0.0.1:8000/docs`

### API Call (Browser or Postman):
Example query: `http://127.0.0.1:8000/ask?query=what is the synopsis about`




