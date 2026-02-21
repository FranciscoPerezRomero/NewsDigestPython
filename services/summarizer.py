from anthropic import Anthropic
from config.settings import ANTHROPIC_APIKEY
def generate_summaries(articles):
    client = Anthropic(api_key=ANTHROPIC_APIKEY)
    message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=150,
    messages=[
        {"role": "user", "content": "Resume esta noticia en 2-3 líneas: [título y descripción]"}
    ]
)
    resumen = message.content[0].text