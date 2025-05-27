## RABBITMQ FOOD DElivery Microservices Demo
this project is small simple food delivery system using Python microservices and RabbitMQ for messaging. Each servcie communicates via RabbitMQ simulating a real life order workflow

##Services 
-** order_services.py**: Places a new food order and publishes it to RabbitMQ.
-**kitchen_service.py**: Listens for new orders, updates the order status to "preparing".
- **delivery_service.py**: Listens for orders and simulates the delivery process.
-**confirmation_service.py**: Listens for orders and prints a confirmation.

## Architecture
All services communicate using a RabbitMq **fanout exchange** called 'orders'. Each service creates its own temporary queue and receives all published orders.

```
order_service.py
        |
     [RabbitMQ Exchange: orders]
      /        |         \
kitchen   delivery   confirmation
service   service     service
```

## Prerequisites 
- Python 3.11 +
- [pika] library (`pip install pika`)
- **RabbitMQ server** (see below)

## RabbitMQ installation

## Ubuntu
```sh
sudo apt update
sudo apt install rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
```
## Check if RabbitMQ is working

```sh
sudo systemctl status rabbitmq-server
```

## Running the Project
1. Start RabbitMQ server (see above)
2. Open a terminal for each service and run:
  ```sh
    python3 kitchen_service.py
    python3 delivery_service.py
    python3 confirmation_service.py  # if you have it
    ```
3. ** In a seperate terminal, place an order:**
    ```sh
    python3 order_service.py
    ```
