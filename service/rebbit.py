import pika


class RebbitMQ:
    __host = 'localhost'

    @staticmethod
    def create_message(photo_url: str, name: str, price: str, url: str) -> str:
        message = f'photo_url: {photo_url}\n\nname: {name}\n\nprice: {price}\n\nurl: {url}'
        return message
    
    @classmethod
    def send_message(cls, photo_url: str, name: str, price: str, url: str) -> None:
        conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=cls.__host, credentials=pika.PlainCredentials('guest', 'guest')
                )
            )
        channel = conn.channel()
        channel.queue_declare(queue='spam', durable=True)
        channel.basic_publish(
            exchange='',
            routing_key='spam',
            body=cls.create_message(
                photo_url=photo_url,
                price=price,
                name=name,
                url=url
            )
        )
        conn.close()

    @classmethod
    def clear_queue(cls):
        conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=cls.__host,
                credentials=pika.PlainCredentials('guest', 'guest')
            )
        )
        channel = conn.channel()
        channel.queue_purge('spam')
        conn.close()

