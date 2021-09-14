from random import choice, uniform, randint
from time import sleep, time
from json import dumps
import paho.mqtt.publish as publish
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import InfluxDBClient

class Analisar:

    def __init__(self):
    	#INICIALIZA AS CONSTANTES PARA ENVIAR DADOS PARA INFLUXDB CLOUD
        self.token = "MetMMIZ5I9XxU03i2DnLwzjaCHKMGOPOPh03SE_3PkhhysoFFCPh4EO-clWGQR65Y63fn5OPRhQxv3n5-RCcIw=="
        self.org = "guilhermedonizettiads@gmail.com"
        self.bucket = "guilhermedonizettiads's Bucket"
        self.client = InfluxDBClient(url="https://us-west-2-1.aws.cloud2.influxdata.com", token=self.token)

    #METODO PARA GERAR OS DADOS (SIMULA A CAPTURA DOS SENSORES)
    def ColetorDeDados(self):
        lugar = ["CPT","DC"] #PREDIO/SALA = CPT/DC
        #coluna+linhas, POSSIVEIS IDENTIFICACAO DE SENSORES
        PMeID = [
            ["AB0102"],["AE0102"],["AH0102"],["AK0102"],["AN0102"],["AR0102"],["AT0102"],
            ["AB0910"],["AE0910"],["AH0910"],["AK0910"],["AN0910"],["AR0910"],["AT0910"],
            ["AB1718"],["AE1718"],["AH1718"],["AK1718"],["AN1718"],["AR1718"],["AT1718"]
                ]
        hostname = '192.168.0.107'
        port = 1883
        print("Enviando.")
        y=0
        #ENVIA DADOS A CADA 0.5 SEG
        while(True):
            print("\n")
            #ENVIA DADO PARA CADA SENSOR
            for i in PMeID:
                ponto = i
                #ENVIA SEMPRE O MESMO VALOR, ALTERA A CADA 45 ENVIOS
                if y%45!=0:
                    temp = 21.41
                    umid = 44.8
                else:
                    temp = uniform(21.2,21.6)
                    umid = uniform(44.5,45.3)
                self.set_mqtt(hostname, port, lugar, ponto, temp, umid)
                y=y+1
                if y==100:
                    y=0
            sleep(0.5)
    
    #METODO PARA EFETUAR O ENVIOPARA O BROKER E CLOUD
    def set_mqtt(self, hostname, port, lugar, ponto, temperatura, umidade):
        sensor = ponto[0] #RECEBE A IDENTIFICACAO DO SENSOR
        temperatura = "%.2f" % temperatura
        umidade = "%.2f" % umidade
        topic = f"{lugar[0]}/{lugar[1]}/{ponto[0]}" #CONFIGURA O TOPICO: PREDIO/SALA/SENSOR
        timeSensor = time() * 1000000000 #RECEBE O INSTANTO EM QUE OS DADOS SAO ENVIADOS
        conteudo = {
            "Temperatura":float(temperatura),
            "Umidade":float(umidade),
            "time":int(timeSensor)
            }
        #PUBLICA NO BROKER MQTT LOCAL 
        publish.single(topic=topic, payload=dumps(conteudo), client_id="EuVejo", hostname=hostname, port=port, auth={'username':'cnpq_project','password':'esferaprotect21D'}, retain=True)
        #PUBLICA NO BUCKET DO INFLUXDB CLOUD
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        data = "Sensores,PM={} Temperatura={},Umidade={} {}".format(ponto[0], temperatura, umidade, int(timeSensor))
        write_api.write(self.bucket, self.org, data)
        #MOSTRA NO TERMINAL OS VALORES ENVIADOS
        print("{} | Valor: {} | Time: {}".format(topic,temperatura, timeSensor))

an = Analisar()
an.ColetorDeDados()

#AUTENTICACAO PARA O PROJETO EM TESTE
#PASSWORD: esferaprotect21D
#USERNAME: cnpq_project