from models import Quote

def search_quotes_by_author(author_name):
    author_quotes = Quote.objects(author__fullname=author_name)
    return author_quotes

def search_quotes_by_tag(tag):
    tag_quotes = Quote.objects(tags=tag)
    return tag_quotes

def search_quotes_by_tags(tags):
    tags_quotes = Quote.objects(tags__in=tags)
    return tags_quotes
