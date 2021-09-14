from random import choice, uniform, randint
from time import sleep, time
from json import dumps
import paho.mqtt.publish as publish
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import InfluxDBClient

class Analisar:

    def __init__(self):
        self.token = "MetMMIZ5I9XxU03i2DnLwzjaCHKMGOPOPh03SE_3PkhhysoFFCPh4EO-clWGQR65Y63fn5OPRhQxv3n5-RCcIw=="
        self.org = "guilhermedonizettiads@gmail.com"
        self.bucket = "guilhermedonizettiads's Bucket"
        self.client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token=self.token)

    def ColetorDeDados(self):
        lugar = ["CPT","DC"]
        #coluna+linhas
        PMeID = [
            ["AB0102"],["AE0102"],["AH0102"],["AJ0102"],["AM0102"],["AP0102"],["AS0102"],
            ["AB0910"],["AE0910"],["AH0910"],["AJ0910"],["AM0910"],["AP0910"],["AS0910"],
            ["AB1718"],["AE1718"],["AH1718"],["AJ1718"],["AM1718"],["AP1718"],["AS1718"]
                ]
        hostname = 'localhost'
        port = 1883
        print("Enviando.")
        y=0
        while(True):
            ponto = choice(PMeID)
            if y%8!=0:
                temp = 21.41
                umid = uniform(44.7,45.2)
            else:
                temp = uniform(20.7,21.7)
                umid = uniform(42.7,44.6)
            self.set_mqtt(hostname, port, lugar, ponto, temp, umid)
            y=y+1
            if y==100:
                y=0
            sleep(0.5)
    
    def set_mqtt(self, hostname, port, lugar, ponto, temperatura, umidade):
        sensor = ponto[0]
        temperatura = "%.2f" % temperatura
        umidade = "%.2f" % umidade
        topic = f"{lugar[0]}/{lugar[1]}/{ponto[0]}"
        timeSensor = time() * 1000000000
        conteudo = {
            "Temperatura":float(temperatura),
            "Umidade":float(umidade),
            "time":int(timeSensor)
            }
        #PUBLICA NO BROKER MQTT LOCAL 
        publish.single(topic=topic, payload=dumps(conteudo), hostname=hostname, port=port, auth={'username':'cnpq_project','password':'esferaprotect21D'}, retain=True)
        #PUBLICA NO BUCKET DO INFLUXDB CLOUD
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        data = "Sensores,PM={} Temperatura={},Umidade={} {}".format(ponto[0], temperatura, umidade, int(timeSensor))
        write_api.write(self.bucket, self.org, data)

        print("{} | Valor: {} | Time: {}".format(topic,temperatura, timeSensor))

an = Analisar()
an.ColetorDeDados()
#esferaprotect21D