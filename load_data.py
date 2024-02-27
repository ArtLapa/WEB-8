import json
from models import Author, Quote

# Підключення до MongoDB
connect('your_db_name', host='your_mongo_connection_string')

# Завантаження даних з файлу authors.json
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()

# Завантаження даних з файлу quotes.json
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

for quote_data in quotes_data:
    author = Author.objects(fullname=quote_data['author']).first()
    quote_data['author'] = author
    quote = Quote(**quote_data)
    quote.save()
