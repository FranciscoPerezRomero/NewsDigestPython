from db.database import get_all_users
from db.database import get_user_tags
from services.summarizer import generate_summaries
from services.processor import title_processor
#* Obtenemos a todos los usuarios registrados
usersInfo = get_all_users()
userNews = []
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
            userNews.append(fetchNews[0])
    else:
        for i in range(0,4):
            print(i)
            # userNews = title_processor(tag)