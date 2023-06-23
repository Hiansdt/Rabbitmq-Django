from __future__ import absolute_import, unicode_literals

from celery import shared_task

import pika
import time

connection_params = pika.ConnectionParameters(
    host='localhost',
    port="5672",
    credentials=pika.PlainCredentials(
        username='guest', 
        password='guest'),
)

@shared_task
def send_message(message):
    channel = pika.BlockingConnection(connection_params).channel()
    channel.channel()
    channel.queue_declare(queue='my_queue', durable=True)
    time.sleep(5)
    channel.basic_publish(body=message, exchange='', routing_key='my_queue')
    channel.close()
    return message
    