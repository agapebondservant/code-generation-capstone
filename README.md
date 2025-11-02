# AI Code Translation Project

## Set up environment

### Jupyter Notebook environment
* Import `eda/jupyter` into your JupyterHub environment.
* From JupyterHub, launch a terminal window and run `pip install -r requirements.txt`.
* To run code_generation_eda.ipynb, also run `pip install -r requirements-eda.txt`. (EDA requires a separate environment.)

### Set up environment variables
* Make a copy of .env-template and rename it to .env.
* Update the .env file with your credentials.

### Deploy the candidate model
Run the following (update the model name, other paramters as needed):
```
pip install vllm hf_transfer
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True
export HF_TOKEN=<your hf token>

python -m vllm.entrypoints.api_server \
--model ibm-granite/granite-8b-code-instruct-4k \
--port 8000 \
--enable-lora \
--dtype float16 \
--max-model-len 4096
```


