from __future__ import absolute_import, unicode_literals

from .models import User

from celery import shared_task

import pika

def my_callback():
    User.objects.create(username='asaddsad')

connection_params = pika.ConnectionParameters(
    host='localhost',
    port="5672",
    credentials=pika.PlainCredentials(
        username='guest', 
        password='guest'),
)

@shared_task
def consume_message():
    channel = pika.BlockingConnection(connection_params).channel()
    channel.queue_declare(queue='my_queue', durable=True)
    channel.basic_consume(
        queue='my_queue',
        auto_ack=True,
        on_message_callback=my_callback
    )