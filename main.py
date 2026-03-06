from db.database import get_all_users, get_user_tags
from services.summarizer import generate_summaries
from services.processor import title_processor
from services.mailer import send_email

def send_daily_digest():
    """Envía el resumen diario de noticias a todos los usuarios."""
    usersInfo = get_all_users()
    userNews = []
    missingNews = 'Noticias no encontradas'
    users_processed = 0
    
    for user in usersInfo:
        userId, userName, userEmail = user
        tags = get_user_tags(userId)
        
        if len(tags) > 1:
            for tag in tags:
                print(tag)
                fetchNews = title_processor(tag)
                if len(fetchNews) >= 1:
                    #* print(f'Tag: {tag}, Noticias encontradas: {len(fetchNews)}')
                    userNews.append(fetchNews[0])
                else:
                    print(missingNews)
        else:
            fetchNews = title_processor(tags)
            if len(fetchNews) >= 1:
                #* print(f'Tag: {tags}, Noticias encontradas: {len(fetchNews)}')
                userNews.extend(fetchNews[0:5])
            else:
                print(missingNews)
        users_processed += 1
        newsResume = generate_summaries(userNews)
        send_email(userName, userEmail, newsResume)
        userNews = []  # Resetear para siguiente usuario
    print(f'Users Processed: {users_processed}')
    
if __name__ == "__main__":
    send_daily_digest()