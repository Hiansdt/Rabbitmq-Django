import json
import pika
import django
from sys import path
from os import environ

path.append('/home/cavalo/Documents/Rabbitmq-Django/consumer/consumer/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'consumer.settings')
django.setup()
from app.models import User

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='my_queue2', durable=True) 

def callback(ch, method, properties, body):
    User.objects.create(username=body.decode("utf-8"))
    print("Messaged Received!")
    print("Message: " + body.decode("utf-8"))


channel.basic_consume(queue='my_queue2', on_message_callback=callback, auto_ack=True)
print("Started consuming...")
channel.start_consuming()