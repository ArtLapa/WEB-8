import json
import pika
from models import Contact

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts_queue')

# Генерація та надсилання фейкових контактів
fake_contacts = [
    {"full_name": "John Doe", "email": "john@example.com"},
    {"full_name": "Jane Smith", "email": "jane@example.com"}
]

for fake_contact in fake_contacts:
    contact = Contact(**fake_contact)
    contact.save()

    # Надіслати ID контакту у чергу
    channel.basic_publish(exchange='',
                          routing_key='contacts_queue',
                          body=str(contact.id))

print("Contacts sent to the queue")

# Закриття з'єднання з RabbitMQ
connection.close()

