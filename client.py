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


def main():
    dev = YaClient('Test_Device_Client')
    reg = YaClient('Test_Registry_Client')

    if settings.USE_DEVICE_LOGIN_PASSWORD:
        dev.start_with_login(settings.DEVICE_ID, settings.DEVICE_PASSWORD)
    else:
        dev.start_with_cert('mptk_register/device1/cert_dev.pem', 'mptk_register/device1/key_dev.pem')

    if settings.USE_REGISTRY_LOGIN_PASSWORD:
        reg.start_with_login(settings.REGISTRY_ID, settings.REGISTRY_PASSWORD)
    else:
        reg.start_with_cert('mptk_register/cert_reg.pem', 'mptk_register/key_reg.pem')

    # res, _ = dev.subscribe(settings.REGISTRY_COMMANDS)
    # if res != mqtt.MQTT_ERR_SUCCESS:
    #     sys.exit("Can't subscribe on [ " + settings.REGISTRY_COMMANDS + " ]")

    # res, _ = reg.subscribe(settings.REGISTRY_EVENTS)
    # if res != mqtt.MQTT_ERR_SUCCESS:
    #     sys.exit("Can't subscribe on [ " + settings.REGISTRY_EVENTS + " ]")

    # res = reg.publish(settings.REGISTRY_COMMANDS, "reg commands")
    # if res != mqtt.MQTT_ERR_SUCCESS:
    #     sys.exit("Can't publish [ " + settings.REGISTRY_COMMANDS + " ]")

    res = dev.publish(settings.REGISTRY_EVENTS, "reg events!!!")
    if res != mqtt.MQTT_ERR_SUCCESS:
        sys.exit("Can't publish [ " + settings.REGISTRY_EVENTS + " ]")

    # dev.wait_subscribed_data()
    # reg.wait_subscribed_data()

    dev.disconnect()
    reg.disconnect()


if __name__ == "__main__":
    main()
