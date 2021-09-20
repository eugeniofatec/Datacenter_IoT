<h1 align="center">Datacenter_IoT</h1>

Monitoramento de temperatura e umidade em datacenter com IoT
Utiliza os softwares Mosquitto, Node-Red, InfluxDB e Grafana

<code>sensores_todos.py</code> é o script Python que simula o envio dos dados.<br>
<code>grafana.json</code> deve ser importado no Grafana para criar a mesma estrutura de dashboard usado no projeto.<br>
<code>flows.json</code> deve ser importado no Node-Red para criar a mesma estrutura de nós usadas no projeto.<br>
<code>mosquitto.conf</code> está na branch <b>Configuracoes</b>, contém as configurações para o Mosquitto.
<br>Sobre a estrutura do InfluxDB, após executar o <b>sensores_todos.py</b> será criado um novo banco e uma nova measurement ("tabela"). As configurações do Grafana já estão compatíveis com a estrutura que será criada no InfluxDB.

<hr>

<h5><b>Uso: </b></h5>

<p>Após a instalação do Grafana, Node-RED, InfluxDB e Mosquitto, as seguintes etapas devem ser executadas:</p><br>
<li>Configure o <code>mosquitto.conf</code> conforme está na branch Configuracoes.</li>
<li>Criar um arquivo <b>senhas.txt</b> conforme está na branch Configuracoes.</li>
<li>Iniciar o servidor do Grafana, Node-RED, InfluxDB e Mosquitto.</li>
<li>Importar os arquivos <code>grafana.json</code> no Grafana e <code>flows.json</code> no Node-RED</li>
<ul>
  <li>O Node-RED após instalado não vem com todos os nós necessários para funcionar, então na hora de importar veja os nós que faltam e faça a instalação deles no <b>manage pallete</b> do Node-RED.</li>
</ul>
<li>Execute o arquivo <code>sensores_todos.py</code>.</li>

<br>

<h5><b>Conferir funcionamento:</b></h5>

<p>Enquanto o arquivo <b>sensores_todos.py</b> executa, observe os dados aparecerem no dashboard importado no Grafana. Também, consulte os dados no InfluxDB executando os comandos:</p>

<code>$ influx</code><br>
<code>$ use Monitoramento</code><br>
<code>$ select * from Sensores</code><br>

Isso deve retornar os dados gerados pelo simulador em Python e mostrar a estrutura do banco.

<br>

<h5><b>Para ativar os servidores:</b></h5>
<p>Os servidores do Grafana, InfluxDB e Node-RED deverão sempre estarem atividados para que o sistema funcione. Ao invés de repetir os comandos no terminal, pode criar os seguintes arquivos:</p><br>

salve como <b>influxdb.sh</b>, para executar: <code>$ sh influxdb.sh</code>
```bash
#!/bin/bash
sudo systemctl start influxdb.service
sudo systemctl status influxdb.service
influx
```
<br>

salve como <b>grafana.sh</b>, para executar: <code>$ sh grafana.sh</code>
```bash
#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server
```
