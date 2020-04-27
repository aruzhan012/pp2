import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='example1')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='example1',body=message)

print (" Sent 'Example 2' ")
channel.close()