# File: order_service/message_producer.py
import pika
import json

def publish_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message)
    )
    connection.close()

# Gửi tin nhắn
if __name__ == "__main__":
    message = {"order_id": 123, "status": "created"}
    publish_message("order_events", message)