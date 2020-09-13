# SE-esp32
Implementação de uma aboradagem para resolução do problrema proposto utlziando MQTT e wifi-manager para o trabalho de SE.

## Proposta da abordagem.
Configurar o acesso do embarcado a uma rede wi-fi, bem como a frequencia de piscagem de dois leds. Para confirmar que o embarcado está em rede deverá ser postada uma mensagem em um broker MQTT a cada 15 segundos.

## Resolução
  A utilização de uma abordagem de wifi-manager como modelo inical foi exencial para o problema, após encontrar o erro de não aceitar simbolos na senha foi concertado.
  
### Wifi-Manager 2.0
  A confguração inicial pode ser fita no arquivo: wifimgr.py
 ```python
  ap_ssid = "WifiKaller" #ssid que ficara para configuração
  ap_password = "kaka1234" #senha para conectar a configuração
  ap_authmode = 3  # WPA2 (modo)
```
No main ela ira inicalizar normlamente.

### MQTT e Controle
  A abordagem utilizada foi ler valores enviados pelos canais Led1 e led2 que são salvos nos respectivos arquivos .txt
   ```python
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
```
A ideia principal é a questão do recebimentos dos valores através do protocolo MQTT.
função de leitura do valor do arquivo.
   ```python
  def led_on_1(): #função para confirgutar o led 2 através dos dados obtidos via mqtt
    ledd = "led1"+".txt"
    while True:
        f = open(ledd)
        print("Led1: " +"Valor:" +f.read())
        f = open(ledd)
        oi =f.read()
        sleep(int(oi))
```
A outra função é a questão do envio a cada 15 segundos para o broker identificando que esta conectado, topico + "/conectado"
```python
  def estou_conectado():
        while True: 
            client.publish(topic="snEwCneZjyGXl7B/conectado", msg="conectado")
            time.sleep(15)
```
A configuração do broker deve ser feita no arquivo (led_controle_mqtt.py), na função inicializar_mqtt_controle, alterando os valores.
```python
 def inicializar_mqtt_controle():
    #dados do broker mqtt (nome do dispositivo, broker, usuario, senha, e porta)
    client = MQTTClient("esp-kaller", "ioticos.org",user="B54eIInVkGEMrEE", password="ZRTczIxVg4wjrLy", port=1883) 
    client.set_callback(sub_cb) 
    client.connect()
    client.subscribe(topic="snEwCneZjyGXl7B/led1") #modificar para o determinado broker
    client2 = client
    client2.subscribe(topic="snEwCneZjyGXl7B/led2") #modificar para o determinado broker
    ......................
    ..........................
```

### Funcionamento
  Cria uma WIFI para configuração caso não consiga se conectar, obtenção de valores através do MQTT para controle individual dos leds e a confirmação (envio de mensagem ao broker) para confirmação que está conectado.
  O valor do dado de cada Led é mostrado no tempo que ele deveria ligar, quando recebe novos valores tambem é informado individualmente.
  



