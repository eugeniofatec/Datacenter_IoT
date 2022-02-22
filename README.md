<h1 align="center">Datacenter_IoT</h1>

Monitoramento de temperatura e umidade em datacenter com IoT
Utiliza os softwares Mosquitto, Node-Red, InfluxDB, Grafana, Node JS e Docker.

<code>sensores_todos.py</code> é o script Python que simula o envio dos dados.<br>

<code>docker-compose.yml</code> é o arquivo de configuração do para a criação dos containes Docker.<br>

<code>docker-init.sh</code> é o arquivo shell de comandos que instala a aplicação.<br>


<hr>

<br>

<h5><b>Uso: </b></h5>

<p>Após a instalação do Docker, execulte o seguinte comando no diretorio do programa:</p>

<code> <b>sudo sh docker-init.sh</b> </code>

<br>

<h5><b>Conferir funcionamento:</b></h5>

<p>Execulte o comando <code>sudo docker ps -a</code> e confira se os conteners  plantaDC, nodeRed, grafana, mosquitto e InfluxDB foram criados e estão ligados.</p>

<br>

<h5><b>Simular sensores:</b></h5>

<p>Para simular a atividade de sensores execute o arquivo <code>sensores_todos.py</code>.</p>


