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





