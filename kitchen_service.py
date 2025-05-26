import pika
import json
import time

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the same exchange
channel.exchange_declare(exchange="orders", exchange_type="fanout")

# Declare a temporary queue and bind to the exchange
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="orders", queue=queue_name)

print("👨‍🍳 Kitchen waiting for orders...")

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"👨‍🍳 Received order #{order['order_id']} - status: {order['order_status']}")
    # Simulate preparing the order
    order['order_status'] = "preparing"
    print(f"🍳 Order #{order['order_id']} is now being prepared!")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()