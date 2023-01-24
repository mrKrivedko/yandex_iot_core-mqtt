import paho__1111


id_register: aremdgkdt0d120oibqb6
id_device: are2m0j8pmv8462gth3m
реестр_iot_password: 8HB+tG;0{CZ4$fLY 


yc iot mqtt publish -u are2m0j8pmv8462gth3m -P 8HB+tG;0{CZ4$fLY -t '$registries/remdgkdt0d120oibqb6/state' -m 'Test data' -q 1

yc iot mqtt publish -u aremdgkdt0d120oibqb6 -P 8HB+tG;0{CZ4$fLY -t "$registries/remdgkdt0d120oibqb6/config" -m "Test data" -q 1
  --username <ID реестра> \
  --password <пароль для реестра> \
  --topic '$registries/<ID реестра>/config' \
  --message 'Test command for all devices' \
  --qos 1
