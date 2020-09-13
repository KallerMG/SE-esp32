import network
from umqtt.simple import MQTTClient
import machine 
import time
from time import sleep
import _thread

global led1 
global led2
def rotina_led(pino,valor):
   led = machinePin(pino,Pin.OUT)
   while True:
       led.value(not led.value())
       sleep(valor)

def led_on_1(): #função para confirgutar o led 2 através dos dados obtidos via mqtt
    ledd = "led1"+".txt"
    while True:
        f = open(ledd)
        print("Led1: " +"Valor:" +f.read())
        f = open(ledd)
        oi =f.read()
        sleep(int(oi))
     
def led_on_2(): #função para confirgutar o led 2 através dos dados obtidos via mqtt
    ledd = "led2"+".txt"
    while True:
        f = open(ledd)
        print("Led2: " +"Valor:" +f.read())
        f = open(ledd)
        oi =f.read()
        sleep(int(oi))
     

def sub_cb(topic, msg):
    if(str(topic,'utf-8') == "snEwCneZjyGXl7B/led1"): #topico para o controle do led 1
        f = open('led1.txt','w')
        f.write(str(msg,'utf-8'))
        f.close()
        print("leddd 1 chegou")
    elif(str(topic,'utf-8') == "snEwCneZjyGXl7B/led2"): #topico para o controle do led 2
        f = open('led2.txt','w')
        f.write(str(msg,'utf-8'))
        f.close()
        print("leddd 2 chegou")
    else:
        print("invalido")
        

        
def inicializar_mqtt_controle():
    #dados do broker mqtt (nome do dispositivo, broker, usuario, senha, e porta)
    client = MQTTClient("esp-kaller", "ioticos.org",user="B54eIInVkGEMrEE", password="ZRTczIxVg4wjrLy", port=1883) 
    client.set_callback(sub_cb) 
    client.connect()
    client.subscribe(topic="snEwCneZjyGXl7B/led1")
    client2 = client
    client2.subscribe(topic="snEwCneZjyGXl7B/led2")
    def estou_conectado():
        while True: 
            client.publish(topic="snEwCneZjyGXl7B/conectado", msg="conectado")
            time.sleep(15)
    t =_thread.start_new_thread(led_on_1,())
    t2 =_thread.start_new_thread(led_on_2,())
    t3 =_thread.start_new_thread(estou_conectado,())

    while True: 
        client.wait_msg()
        time.sleep(1)
        client2.check_msg()
        time.sleep(1)  
