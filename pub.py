from paho.mqtt.client import MQTT_ERR_SUCCESS
import os
import sys

import settings
from ya_client import YaClient


def main():
    dev = YaClient(settings.DEVICE_NAME)
    reg = YaClient(settings.REGISTRY_NAME)

    if settings.USE_DEVICE_LOGIN_PASSWORD:
        dev.start_with_login(settings.DEVICE_ID, settings.DEVICE_PASSWORD)
    else:
        dev.start_with_cert(settings.DEVICE_CERT, settings.DEVICE_KEY)

    # if settings.USE_REGISTRY_LOGIN_PASSWORD:
    #     reg.start_with_login(settings.REGISTRY_ID, settings.REGISTRY_PASSWORD)
    # else:
    #     reg.start_with_cert('mptk_register/cert_reg.pem', 'mptk_register/key_reg.pem')

    # res, _ = dev.subscribe(settings.REGISTRY_COMMANDS)
    # if res != mqtt.MQTT_ERR_SUCCESS:
    #     sys.exit("Can't subscribe on [ " + settings.REGISTRY_COMMANDS + " ]")

    # res, _ = reg.subscribe(settings.REGISTRY_EVENTS)
    # if res != mqtt.MQTT_ERR_SUCCESS:
    #     sys.exit("Can't subscribe on [ " + settings.REGISTRY_EVENTS + " ]")

    # res = reg.publish(settings.REGISTRY_COMMANDS, "reg commands")
    # if res != MQTT_ERR_SUCCESS:
    #     sys.exit("Can't publish [ " + settings.REGISTRY_COMMANDS + " ]")
    payload = input()

    res = dev.publish(settings.REGISTRY_EVENTS, payload)
    if res != MQTT_ERR_SUCCESS:
        sys.exit("Can't publish [ " + settings.REGISTRY_EVENTS + " ]")

    # dev.wait_subscribed_data()
    # reg.wait_subscribed_data()

    dev.disconnect()
    # reg.disconnect()


if __name__ == "__main__":
    main()
