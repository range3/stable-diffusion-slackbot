# Stable Diffusion Slackbot
Stable Diffusion  
https://github.com/CompVis/stable-diffusion

## Usage
### Install Python libraries using conda
```bash
conda env create -f environment.yaml
conda activate ldm
```

### Log in to HuggingFaceHub with an account that agrees to the stable diffusion license
```bash
huggingface-cli login
```

### required environment variables
```bash
export SLACK_BOT_TOKEN=xoxb-xxxxxx
export SLACK_APP_TOKEN=xapp-xxxxxx
```

### run bot server
```bash
python run.py
```
