from api.news_client import fetch_news
from db.database import get_user_tags
def title_processor(tag):
    #* Diccionario para guardar los articulos
    unique_Articles = []
    #* Obtenemos articulos
    dataDict = fetch_news(tag)
    #* Ciclo para recorrer todos los articulos encontrados
    for article in dataDict['articles']:
        #* Cuando no hay articulos
        if len(unique_Articles) == 0:
            unique_Articles.append(article)
        else:
            duplicate_item = False
            for saved_article in unique_Articles: 
                if titles_Similar(article['title'],saved_article['title']):
                    duplicate_item = True
                    break
            if not duplicate_item:
                unique_Articles.append(article)
    return unique_Articles

def titles_Similar(new_article, articleStorage):
    new_article = set(new_article.lower().split(" "))
    articleStorage = set(articleStorage.lower().split(" "))
    intersection = new_article & articleStorage
    union = new_article | articleStorage
    #* Se multiplica por 100 por que el resultado es en porcentaje 
    similarPercent =   len(intersection) / len(union) * 100
    return True if similarPercent >= 50 else False