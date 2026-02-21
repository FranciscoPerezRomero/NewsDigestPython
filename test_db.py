from services.processor import title_processor

result = title_processor(2)  # Usa el ID de un usuario que tengas
print(result)
print(f"Total de artículos únicos: {len(result)}")
print("\nPrimeros 5 títulos únicos:")
for i, article in enumerate(result[:5]):
    print(f"{i+1}. {article['title']}")
    