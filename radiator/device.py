import puka

class Device:
    """ Object for control remote device """
    def __init__(self):
        self.producer = puka.Client("amqp://10.0.0.20/")
        send_promise = self.producer.connect()
        self.producer.wait(send_promise)

    def _send(self,cmd):
        send_promise = self.producer.basic_publish(exchange='radiator', routing_key='radiator', body=cmd)
        self.producer.wait(send_promise)

    def light_on(self):
        self._send('L:1')

    def light_off(self):
        self._send('L:0')

