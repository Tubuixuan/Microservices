# File: product_service/message_consumer.py
import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")
    # Xử lý tin nhắn tại đây

def consume_messages(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )
    print(f"Waiting for messages on queue: {queue_name}")
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages("order_events")