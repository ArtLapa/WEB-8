import json
import pika
from models import Contact

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contacts_queue')

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()

    if contact:
        # Імітація надсилання повідомлення по email
        print(f"Sending email to {contact.email}")

        # Оновлення поля is_message_sent
        contact.is_message_sent = True
        contact.save()

# Вказати функцію обробник
channel.basic_consume(queue='contacts_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
