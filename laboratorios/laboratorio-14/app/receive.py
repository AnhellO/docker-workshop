import pika, sys, os

def main():
    credentials = pika.PlainCredentials('therabbit', 'secret123')
    parameters = pika.ConnectionParameters(host='rabbitmq', port=5672, virtual_host='/', credentials=credentials)
    print(f'Parameters: {parameters}')
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f' [x] Received {body}')

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)