import pika
import time


def callback(ch, method, properties, body):
    print ("Received: {}".format(body))
    time.sleep( body.count(b'.') )
    print( "Done")

connection = pika.BlockingConnection(pika.ConnectionParameters ('localhost'))

channel = connection.channel()

channel.queue_declare(queue='example1')
channel.basic_consume('example1', auto_ack=True, on_message_callback=callback)
print (' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()