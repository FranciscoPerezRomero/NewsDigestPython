from anthropic import Anthropic
from config.settings import ANTHROPIC_APIKEY
#* Recibe diccionario
def generate_summaries(articles):
    client = Anthropic(api_key=ANTHROPIC_APIKEY)
    for article in articles:
        try:
            message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=150,
            messages=[
                {"role": "user", "content": f"Resume esta noticia en 2-3 líneas: {article['title']} y {article['description']}"}
                ]
            )
            resumen = message.content[0].text
            article['summary'] = resumen
        except Exception as e:
            article['summary'] = article['description']
    return articles