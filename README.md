# multi-file-rag
![legend and notes](schema/image.png)
![deployment notes](schema/image-1.png)
![code map](schema/image-2.png)
![ingestion sequence](schema/image-3.png)
![query sequence](schema/image-4.png)
![overview](schema/image-5.png)


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

### llm model link: https://drive.google.com/file/d/1NQCB9rgcKClzkwTBHWbHCZYGB_7bpITc/view?usp=sharing
(save the same in the model directory)

## To run the pipeline (watcher):
`python config.py`

## To run the FAST API:
`uvicorn api.main:app --reload`

### Open browser:
`http://127.0.0.1:8000/docs`


## On uploading or changes in the file in the document directory, RAG implementaion can be viewed

### API Call (Browser or Postman):
Example query: `http://127.0.0.1:8000/ask?query=what is the synopsis about`



## To scrap urls from the page

### Give executable permission
`chmod +x crawl_links.sh`

### Useage
`./crawl_links.sh <url>`

while the watcher/pipeline is running (to detect file change)




