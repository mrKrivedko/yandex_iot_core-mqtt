import paho.mqtt.client as mqtt
import sys
import threading
from enum import IntEnum

import settings


class Qos(IntEnum):
    AT_MOST_ONCE = 0
    AT_LEAST_ONCE = 1


class YaClient:

    def __init__(self, client_id):
        self.received = threading.Event()
        self.qos = Qos.AT_LEAST_ONCE
        self.client = mqtt.Client(client_id)
        self.client.user_data_set(self.received)
        self.client.on_message = self.on_message

    def start_with_cert(self, cert_file, key_file):
        self.client.tls_set(settings.ROOTCA_PATH, cert_file, key_file)
        self.client.connect(settings.MQTT_SERVER, settings.MQTT_PORT, 60)
        self.client.loop_start()

    def start_with_login(self, login, password):
        self.client.tls_set(settings.ROOTCA_PATH)
        self.client.username_pw_set(login, password)
        self.client.connect(settings.MQTT_SERVER, settings.MQTT_PORT, 60)
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()

    @staticmethod
    def on_message(client, userdata, message):
        print("Received message '" + str(message.payload) + "' on topic '"
              + message.topic + "' with QoS " + str(message.qos))
        userdata.set()

    def publish(self, topic, payload):
        rc = self.client.publish(topic, payload, self.qos)
        rc.wait_for_publish()
        return rc.rc

    def subscribe(self, topic):
        return self.client.subscribe(topic, self.qos)

    def wait_subscribed_data(self):
        self.received.wait()
        self.received.clear()
