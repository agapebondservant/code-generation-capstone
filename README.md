# AI Code Translation Project

## Set up environment

### Jupyter Notebook environment
* Import `eda/jupyter` into your JupyterHub environment.
* From JupyterHub, launch a terminal window and run `pip install -r requirements.txt`.
* To run code_generation_eda.ipynb, also run `pip install -r requirements-eda.txt`. (EDA requires a separate environment.)
* To run code_generation_agentic.ipynb, instead run `pip install --ignore-installed -r requirements-agentic.txt`.

### Set up environment variables
* Make a copy of .env-template and rename it to .env.
* Update the .env file with your credentials.

### Deploy the baseline model
Run the following (update the model name, other parameters as needed):
```
pip install vllm hf_transfer flashinfer-python transformers==4.56.0
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
export HF_TOKEN=<your hf token>

python -m vllm.entrypoints.openai.api_server \
--model ibm-granite/granite-4.0-h-tiny \
--port 8000 \
--dtype bfloat16 \
--max-model-len 128000 \
--trust-remote-code \
--gpu-memory-utilization 0.9
```

### Deploy the candidate models
At the time of deployment, there are currently unresolved issues with deploying the Granite 4 models with vLLM: https://github.com/vllm-project/vllm/issues/27620
Hence, use **HuggingFace Inference Endpoints** to deploy the candidate models 
(requires a paid plan): https://huggingface.co/inference

### Deploy the demo app
To run the app locally:
  1. Set up a virtual environment: python3.12 -m venv venv 
  2. Install dependencies: pip install -r requirements.txt 
  3. Start the app: python3 -m streamlit run app.py

