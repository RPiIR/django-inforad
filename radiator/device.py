import puka

class Device:
    """ Object for control remote device """
    def __init__(self):
        self.producer = puka.Client("amqp://127.0.0.1/")
        send_promise = self.producer.connect()
        self.producer.wait(send_promise)
        exchange_promise = self.producer.exchange_declare(exchange='radiator', type='topic')
        self.producer.wait(exchange_promise)

    def _send(self,cmd):
        send_promise = self.producer.basic_publish(exchange='radiator', routing_key='radiator', body=cmd)
        self.producer.wait(send_promise)

    def light_on(self):
        self._send('L:1')

    def light_off(self):
        self._send('L:0')

