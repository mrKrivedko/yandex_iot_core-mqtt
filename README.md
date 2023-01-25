# yandex_iot_core-mqtt

## Пример работы с mqtt сервером с использованием библиотеки paho.
[Установка библиотеки paho](https://github.com/eclipse/paho.mqtt.python)

    python -m venv venv
    source venv/Script/activate
    pip install paho-mqtt

[Сертификат удостоверяющего
центра](https://storage.yandexcloud.net/mqtt/rootCA.crt) включен в пример
в виде файла на диске rootCA.crt.

Для работы примера нужно создать
[реестр](https://cloud.yandex.ru/docs/iot-core/quickstart#create-registry) и
[устройство](https://cloud.yandex.ru/docs/iot-core/quickstart#create-device).

Пример фактически делают эхо, то есть посланное в `$devices/<ID
устройства>/events` возвращается клиенту посредством подписки на этот топик
от имени реестра и выводится на консоль.

Поддерживаются два спосба
[авторизации](https://cloud.yandex.ru/docs/iot-core/concepts/authorization),
сертификаты и логин/пароль.


#### Сертификаты

В примере используются два
[сертификата](https://cloud.yandex.ru/docs/iot-core/quickstart#create-ca) - один
для устройства, один для реестра.

Расположение на диске:

    certs structure:
      /my_registry        Registry directory |currentDir|. Run samples from here.
      - /device          Concrete device cert directory.
      |  - dev.crt
      |  - dev.key
      - reg.crt
      - reg.key

Пример ищет сертификаты относительно current working directory, **поэтому
запускать их нужно в папке с сертификатами** (`my_registry` на схеме).


#### Логин/пароль

Нужно сгенерировать пароль для
[реестра](https://cloud.yandex.ru/docs/iot-core/operations/password/registry-password)
и для
[устройства](https://cloud.yandex.ru/docs/iot-core/operations/password/device-password).
Логины реестра и устройства это их `ID`.

## Платформа Яндекс.Облако предоставляет сервис Yandex IoT Core, который обеспечивает двусторонний обмен сообщениями с устройствами по протоколу MQTT. ##

Если вам не знакомы принципы работы протокола MQTT, а также связанными с ними терминами, то вы можете прочитать статью на нашем сайте: 
http://www.rusavtomatika.com/mqtt/.

1. Вводная теоретическая часть
Ссылка на документацию яндекс сервиса
https://cloud.yandex.ru/docs/iot-core/
2. Практическая часть
 План работы:  
1. Установка сертификатов  
2. Активация пробного периода в  Яндекс.Облаке  
3. Создание реестра в  Яндекс.Облаке  
4. Подключение устройств в  Яндекс.Облаке  
5. Создание проекта в EasyBuilder Pro для панели оператора  
6. Установка MQTT.fx (windows-приложение MQTT-клиент)
7. Тестирование работы

В сервисе Yandex IoT Core у каждого устройства и реестра должен быть свой личный сертификат. Давайте создадим два сертификата: для реестра и для устройства. 
Для этого нам понадобится программа OpenSSL. 

Есть два варианта получения этой программы: 
1. Скачать с официального сайта исходный код и скомпилировать его. 
2. Скачать уже готовую программу со стороннего сайта. В нашем случае мы скачаем готовую программу.
- Перейдите по ссылке: 
<https://slproweb.com/products/Win32OpenSSL.html>
- Выберите разрядность вашей системы и скачайте файл. 
- Установите приложение. Все настройки оставьте по умолчанию. 
На последнем шаге можно отказаться от материальной помощи разработчикам, сняв галочку.
- Теперь необходимо задать глобальные переменные в операционной системе. Для этого перейдите в: “Панель управления” - ”Система” - ”Дополнительные параметры системы”-”Переменные среды”.
- В переменную OPENSSL_CONF вписываем путь до файла конфигурации _openssl.cfg_. 
- В переменную Path вписываем путь до директории bin в корневой папке программы.
Создайте на диске "С" папку с названием "SertFolder". 
В ней мы будем создавать файлы сертификатов.
- Запустите стандартную программу _Windows PowerShell_
- Перейдите в папку <c:\SertFolder\>
Запустим openssl с параметрами, чтобы сгенерировать сертификаты для реестра. 


    openssl req -x509 -newkey rsa:4096 -keyout key_reg.pem -out cert_reg.pem -nodes -days 365 -subj '/CN=localhost'


Создались два файла: ключ - *key_reg.pem* и сертификат - cert_reg.pem.  
Эти файлы мы будем использовать для реестра.
Теперь запустите openssl  с другими названиями файлов в параметрах, чтобы сгенерировать сертификаты для устройства. 

    openssl req -x509 -newkey rsa:4096 -keyout key_dev.pem -out cert_dev.pem -nodes -days 365 -subj '/CN=localhost'


# Активация пробного периода в  Яндекс.Облаке #
1. Зайдите на страницу https://console.cloud.yandex.ru/ 
2. Активируйте пробный период. 
Для этого потребуется ввести данные вашей кредитной карты. 
## Создание реестра в  Яндекс.Облаке ##
- В консоли управления Яндекс.Облака найдите в левой колонке пункт "IoT Core" и перейдите на страницу сервиса.
- Нажмите кнопку [Создать реестр], введите название реестра и загрузите файл сертификата реестра. В конце нажмите кнопку [Создать].
## Подключение устройства в  Яндекс.Облаке ##
- Перейдите в созданный реестр, щелкнув по нему из списка. 
- В левом меню выберите "Устройство"  и нажмите на “Добавить устройство”.
- Введите название и загрузите сертификат устройства, который вы создали ранее.
## Создание проекта в EasyBuilder Pro для панели оператора.
- Создайте проект в Easybuilder Pro для вашей панели оператора. 
В главном окне проекта размещаем четыре цифровых объекта, в одном из которых включаем возможность ввода. К цифровым объектам добавляем пояснительные метки.
В цифровых объектах проставляем адреса от LW-100 до 103
Публикация данных в топик событий    -   LW-100
Подписка на топик команд             -   LW-101
Состояние                            -   LW-102
Ошибки                               -   LW-103
Перейдите на вкладку [IIoT/энергетика] - [MQTT]. Установите галочку [Включить] и нажмите [Настройки]
Укажите домен брокера Yandex и порт. Для этого около поля IP поставим галочку “Использовать имя домена” и пропишем адрес.

    - `Домен: mqtt.cloud.yandex.net` 
    - `Порт: 8883` 
    - `Укажите протокол: MQTT v3.1.1` 

Во вкладке [Адрес] пропишите адрес нашего объекта "состояние подключения", в нашем случае LW-102.
Во вкладке [TLS/SSL] нажмите на галочку включить, и после поставьте галочки [проверка сервера] и [проверка клиента].
Теперь нужно загрузить "сертификат удостоверяющего центра Яндекса", "сертификат устройства" и "ключ устройства".
Скачайте с сайта Яндекса “Сертификат удостоверяющего центра” (<https://cloud.yandex.ru/docs/iot-core/concepts/mqtt-properties>)

Установка MQTT.fx 
Это приложение нам понадобится для демонстрации работы MQTT.
Оно будет выполнять роль реестра. Скачайте приложение с сайта: 
<https://mqttfx.jensd.de/index.php/download> 
Установите и запустите его.
