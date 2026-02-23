# test_summarizer.py
from services.summarizer import generate_summaries

# Artículos de prueba
test_articles = [
    {
        'title': 'OpenAI lanza GPT-5',
        'description': 'La nueva versión presenta mejoras significativas en razonamiento.',
        'url': 'https://ejemplo.com/1'
    },
    {
        'title': 'Tesla anuncia Model 4',
        'description': 'El vehículo eléctrico más avanzado hasta la fecha.',
        'url': 'https://ejemplo.com/2'
    }
]

result = generate_summaries(test_articles)

for article in result:
    print(f"Título: {article['title']}")
    print(f"Resumen: {article['summary']}")
    print("---")