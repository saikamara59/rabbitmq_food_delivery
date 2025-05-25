# order_service.py
import pika
import json
import uuid

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Declare a fanout exchange for broadcasting
channel.exchange_declare(exchange="orders", exchange_type="fanout")

# Simulate placing an order
order = {
    "order_id": str(uuid.uuid4())[:8],
    "item": "Bed Stuy Fish Fry",
    "size": "large",
    "toppings": ["pepperoni", "mushrooms", "extra cheese"],
    "address": "123 Main St, Brooklyn, NY",
    "quantity": 2
}

# Publish order to exchange
channel.basic_publish(
    exchange="orders",
    routing_key="",  # Fanout doesn't use routing keys
    body=json.dumps(order)
)

print(f"🍕 Sent order: {order}")
connection.close()
# testing purposes 