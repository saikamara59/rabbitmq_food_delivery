# delivery_service.py
import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the same exchange
channel.exchange_declare(exchange="orders", exchange_type="fanout")

# Declare a temporary queue and bind to the exchange
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="orders", queue=queue_name)

print("🚚 Waiting for delivery orders...")

# Handle received messages
def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"📦 Delivering Order #{order['order_id']}: {order['item']} (x{order['quantity']})")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
