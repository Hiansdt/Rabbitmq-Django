from __future__ import absolute_import, unicode_literals

from .models import User

from celery import shared_task

import pika

def my_callback():
    print("aqui....")
    User.objects.create(username='asaddsad')

connection_params = pika.ConnectionParameters(
    host='127.0.0.1',
    port="5672",
    virtual_host='/',
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