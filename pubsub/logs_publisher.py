#!/usr/bin/env python
import pika
import sys
import time

time.sleep(30)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='pb-rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()


time.sleep(200)
