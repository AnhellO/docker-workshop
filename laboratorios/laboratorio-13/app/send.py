import pika, time

credentials = pika.PlainCredentials('therabbit', 'secret123')
parameters = pika.ConnectionParameters(host='rabbitmq', port=5672, virtual_host='/', credentials=credentials)
print(f'Parameters: {parameters}')
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body=f'Hello World #{i}!')
    print(f" [{i}] Sent 'Hello World!'")
    time.sleep(2)

connection.close()