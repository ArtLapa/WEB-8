import redis
import re
from models import Quote

# Підключення до Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def search_quotes(query):
    cached_result = redis_client.get(query)
    if cached_result:
        return eval(cached_result)  # Важливо: перевірте безпеку перед використанням eval

    result = []

    if re.match(r'^name:\w+', query):
        author_name = query.split(':')[1]
        result = search_quotes_by_author(author_name)
    elif re.match(r'^tag:\w+', query):
        tag = query.split(':')[1]
        result = search_quotes_by_tag(tag)
    elif re.match(r'^tags:\w+(,\w+)+', query):
        tags = query.split(':')[1].split(',')
        result = search_quotes_by_tags(tags)

    # Кешування результату на 60 секунд
    redis_client.setex(query, 60, str(result))
    return result
