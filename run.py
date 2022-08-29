import os
import io
import logging
from pprint import pprint
import slack_sdk
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from torch import autocast
from diffusers import StableDiffusionPipeline

# logging.basicConfig(level=logging.DEBUG)

BOT_CHANNEL='C040S9F4FHN'
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
pipe = pipe.to(device)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
)

@app.event(event={"type": "message","subtype": None,}, matchers=[lambda body: body['event']['channel'] == BOT_CHANNEL])
def handle_message(logger: logging.Logger, event, client: slack_sdk.web.client.WebClient):
    prompt = event["text"]
    with autocast("cuda"):
        image = pipe(prompt, guidance_scale=7.5)["sample"][0]
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        client.files_upload(file=image_bytes.getvalue(), channels=BOT_CHANNEL)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(
        app=app,
        app_token=os.environ["SLACK_APP_TOKEN"],
        trace_enabled=True,
    ).start()
