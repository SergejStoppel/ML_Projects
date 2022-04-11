import pika
import uuid

long_text = 'The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the ' \
            'tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During ' \
            'its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made ' \
            'structure in the world, a title it held for 41 years until the Chrysler Building in New York City was ' \
            'finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a ' \
            'broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 ' \
            'metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure ' \
            'in France after the Millau Viaduct.'

class SummarizeClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response


summary_rpc = SummarizeClient()

response = summary_rpc.call(long_text)
print(response)
