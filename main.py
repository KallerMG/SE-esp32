import wifimgr
from time import sleep
import machine
import _thread
import led_controle_mqtt

try:
  import usocket as socket
except:
  import socket

led = machine.Pin(2, machine.Pin.OUT)

wlan = wifimgr.get_connection()
if wlan is None:
    print("Não foi possível inicializar a conexão.")
    while True:
        pass  

# codigo do do controle  apartir daqui.

t =_thread.start_new_thread(led_controle_mqtt.inicializar_mqtt_controle,())


