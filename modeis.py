from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField, connect

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    is_message_sent = BooleanField(default=False)

