import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Server:

MQTT_SERVER = 'mqtt.cloud.yandex.net'
MQTT_PORT = 8883
ROOTCA_PATH = os.path.abspath('rootCA.crt')

# Certificates directory:

# CERT_REG = os.path.join(BASE_DIR, 'register')
# CERT_DEV = os.path.join(CERT_REG, 'device')

CERT_REG = os.path.join(BASE_DIR, 'mptk_register')
CERT_DEV = os.path.join(CERT_REG, 'device1')

# Devices:

DEVICE_ID = os.getenv('DEVICE_ID', default='areu64lk2ls1dadeea1f')
DEVICE_PASSWORD = os.getenv('DEVICE_PASSWORD', default='8HB+tG;0{CZ4$fLY')
DEVICE_NAME = 'Test_Device_Client'
DEVICE_CERT = os.path.join(CERT_DEV, 'cert_dev.pem')
DEVICE_KEY = os.path.join(CERT_DEV, 'key_dev.pem')


# Registry:

REGISTRY_ID = os.getenv('REGISTRY_ID', default='aredobdlvvrfb4c4b098')
REGISTRY_PASSWORD = os.getenv('REGISTRY_PASSWORD', default='8HB+tG;0{CZ4$fLY')
REGISTRY_NAME = "Test_Registry_Client"
REGISTRY_CERT = os.path.join(CERT_REG, 'cert_reg.pem')
REGISTRY_KEY = os.path.join(CERT_REG, 'key_reg.pem')

# Topics:

REGISTRY_COMMANDS = "$registries/" + REGISTRY_ID + "/commands"
REGISTRY_EVENTS = "$registries/" + REGISTRY_ID + "/events"
REGISTRY_STATE = '$registries/' + REGISTRY_ID + '/state'
REGISTRY_CONFIG = '$registries/' + REGISTRY_ID + '/config'

DEVICE_CONFIG = '$devices/' + DEVICE_ID + '/config'
DEVICE_STATE = '$devices/' + DEVICE_ID + '/state'
DEVICE_EVENTS = '$devices/' + DEVICE_ID + '/events'
DEVICE_COMMANDS = '$devices/' + DEVICE_ID + '/commands'

MONITORING = '$monitoring/' + DEVICE_ID + '/json'

# False means use certificates

USE_DEVICE_LOGIN_PASSWORD = False
USE_REGISTRY_LOGIN_PASSWORD = False
