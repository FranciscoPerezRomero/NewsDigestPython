from datetime import datetime
from config.settings import NEWS_APIKEY
import requests
def fetch_news(topics, language='es', country='mx'):
    #* Url API
    url = 'https://newsapi.org/v2/everything'
    #* Fecha actual
    timestamp = datetime.now().isoformat()
    

    try: #* Query o petición
        query = requests.get(url, params={
            'q' : ' OR '.join(topics),
            'language' : language,
            'apikey': NEWS_APIKEY
        })
        query.raise_for_status()
        #* Paser de json
        data = query.json()
        dataDict = {'status':data['status'],
                    'total_results':data['totalResults'],
                    'fetched_at':timestamp,
                    'articles':data['articles']}
        
        return dataDict 
    except requests.exceptions.ConnectionError as e:
        raise ValueError(e)
    except requests.exceptions.HTTPError as e:
        raise ValueError(e)