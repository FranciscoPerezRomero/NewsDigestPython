from db.database import get_all_users
from db.database import get_user_tags
from services.summarizer import generate_summaries
from services.processor import title_processor
#* Obtenemos a todos los usuarios registrados
usersInfo = get_all_users()
userNews = []
missingNews = 'Noticias no encontradas'
print(usersInfo)
#* Iteramos la lista de usuarios
for user in usersInfo:
    #* Destructuramos y guardamos información del usuario
    userId, userName, userEmail = user
    tags = get_user_tags(userId)
    if len(tags) > 1:
        for tag in tags:
            print(tag)
            fetchNews = title_processor(tag)
            if len(fetchNews) >= 1:
                print(f'Tag: {tag}, Noticias encontradas: {len(fetchNews)}')
                userNews.append(fetchNews[0])
            else:
                print(missingNews)
    else:
        fetchNews = title_processor(tags)
        if len(fetchNews) >= 1:
            print(f'Tag: {tags}, Noticias encontradas: {len(fetchNews)}')
            userNews.extend(fetchNews[0:5])
        else:
            print(missingNews)
    newsResume = generate_summaries(userNews)
    print(newsResume[0]['summary'])