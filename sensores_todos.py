from random import choice, uniform, randint
from time import sleep, time
from json import dumps
import paho.mqtt.publish as publish


class Analisar:
    def __init__(self):

        self.hall = [
            ["0102"],
            ["0910"],
            ["1718"],
        ]

        self.columns = [
            ["AB"],
            ["AE"],
            ["AH"],
            ["AK"],
            ["AN"],
            ["AR"],
        ]

        self.hallStatus = {}
        for i in self.hall:
            self.hallStatus[i[0]] = {
                "tempValue": 21.2,
                "umidValue": 44.0,
                "tempOscillation": 0,
                "umidOscillation": 0,
            }

    # MÉTODO PARA GERAR OS DADOS DOS CORREDORES (SIMULA A CAPTURA DOS SENSORES EM CONJUNTOS DE CADA CORREDOR)
    def ColetorDeDadosLinear(self):

        lugar = ["CPT", "DC"]  # PREDIO/SALA = CPT/DC

        # corredores e coluna, VARIÁVEIS DE IDENTIFICACAO DE SENSORES
        hall = self.hall
        columns = self.columns

        hostname = "127.0.0.1"
        port = 1884

        print("Coletor De Dados Linear")
        print("Enviando.")

        # ENVIA DADOS A CADA 0.8 SEG
        while True:
            print("\n")

            # DEFINE DADO PARA CADA CORREDOR
            for i in hall:
                ponto = i

                # ENVIA UM VALOR  DIFERENTE  OU  IGUAL DE  ACORDO COM A OSCILAÇÃO  DEFINIDA ALEATORIAMENTE
                sensorStatus = self.hallStatus[ponto[0]]

                for e in [
                    ["tempOscillation", "tempValue"],
                    ["umidOscillation", "umidValue"],
                ]:
                    if sensorStatus[e[0]] == 0:
                        oscillation = randint(1, 100)
                        if oscillation >= 1 and oscillation <= 10:
                            sensorStatus[e[0]] = 1
                        if oscillation >= 90 and oscillation <= 100:
                            sensorStatus[e[0]] = 2
                    else:
                        if sensorStatus[e[0]] == 1:
                            sensorStatus[e[1]] = float(
                                "%.2f"
                                % (sensorStatus[e[1]] + (1 + (randint(0, 9) / 10)))
                            )
                        elif sensorStatus[e[0]] == 2:
                            sensorStatus[e[1]] = float(
                                "%.2f"
                                % (sensorStatus[e[1]] - (1 + (randint(0, 9) / 10)))
                            )

                        oscillation = randint(1, 100)
                        if oscillation >= 20 and oscillation <= 95:
                            sensorStatus[e[0]] = 0
                        elif oscillation >= 95 and oscillation <= 100:
                            if sensorStatus[e[0]] == 1:
                                sensorStatus[e[0]] = 2
                            else:
                                sensorStatus[e[0]] = 1
                    if sensorStatus[e[1]] < 18:
                        sensorStatus[e[1]] = 19
                        sensorStatus[e[0]] = 1

                    elif sensorStatus[e[1]] > 55:
                        sensorStatus[e[1]] = 54
                        sensorStatus[e[0]] = 2

                self.hallStatus[ponto[0]] = sensorStatus

                temp = self.hallStatus[ponto[0]]["tempValue"]
                umid = self.hallStatus[ponto[0]]["umidValue"]

                # ENVIA DADO PARA CADA SENSOR
                for column in columns:
                    self.set_mqtt(
                        hostname, port, lugar, (column[0] + ponto[0]), temp, umid
                    )

            sleep(0.5)

    # METODO PARA GERAR OS DADOS (SIMULA A CAPTURA DOS SENSORES)
    def ColetorDeDados(self):
        lugar = ["CPT", "DC"]  # PREDIO/SALA = CPT/DC

        # coluna+linhas, POSSIVEIS IDENTIFICACAO DE SENSORES
        PMeID = []
        for i in self.hall:
            for e in self.columns:
                PMeID = PMeID + [(e[0] + i[0])]

        hostname = "127.0.0.1"
        port = 1884

        print("Coletor De Dados Constante")
        print("Enviando.")

        y = 0
        # ENVIA DADOS A CADA 0.8 SEG
        while True:
            print("\n")
            # ENVIA DADO PARA CADA SENSOR
            for i in PMeID:
                ponto = i
                # ENVIA SEMPRE O MESMO VALOR, ALTERA A CADA 45 ENVIOS
                if y % 45 != 0:
                    temp = 21.41
                    umid = 44.8
                else:
                    temp = uniform(21.2, 21.6)
                    umid = uniform(44.5, 45.3)
                self.set_mqtt(hostname, port, lugar, ponto, temp, umid)
                y = y + 1
                if y == 100:
                    y = 0

            sleep(0.5)

    # METODO PARA EFETUAR O ENVIOPARA O BROKER E CLOUD
    def set_mqtt(self, hostname, port, lugar, ponto, temperatura, umidade):

        # RECEBE A IDENTIFICACAO DO SENSOR
        sensor = ponto
        temperatura = "%.2f" % temperatura
        umidade = "%.2f" % umidade
        topic = (
            f"{lugar[0]}/{lugar[1]}/{ponto}"  # CONFIGURA O TOPICO: PREDIO/SALA/SENSOR
        )

        # RECEBE O INSTANTE EM QUE OS DADOS SAO ENVIADOS
        timeSensor = time() * 1000000000
        conteudo = {
            "Temperatura": float(temperatura),
            "Umidade": float(umidade),
            "time": int(timeSensor),
        }
        # PUBLICA NO BROKER MQTT LOCAL
        publish.single(
            topic=topic,
            payload=dumps(conteudo),
            client_id="EuVejo",
            hostname=hostname,
            port=port,
            auth={"username": "cnpq_project", "password": "esferaprotect21D"},
            retain=True,
        )

        # MOSTRA NO TERMINAL OS VALORES ENVIADOS
        print(
            "{} | temperatura: {} | umidade: {} | Time: {}".format(
                topic, temperatura, umidade, timeSensor
            )
        )


an = Analisar()
an.ColetorDeDadosLinear()
# an.ColetorDeDados()

# AUTENTICACAO PARA O PROJETO EM TESTE
# PASSWORD: esferaprotect21D
# USERNAME: cnpq_project
