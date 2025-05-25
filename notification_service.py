# notification_service.py
import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare the same exchange
channel.exchange_declare(exchange="orders", exchange_type="fanout")

# Create and bind to a temporary queue
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="orders", queue=queue_name)

print("📬 Waiting to send order notifications...")

# Handle incoming messages
def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"📲 Notification: Order #{order['order_id']} placed for {order['item']} (x{order['quantity']})")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
