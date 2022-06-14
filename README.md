<h1 align="center">Datacenter_IoT</h1>
 
Monitoramento de temperatura e umidade em datacenter com IoT
Utiliza os softwares Mosquitto, Node-Red, InfluxDB, Grafana, Node JS, Ansible e Docker.
 
<code>sensores_todos.py</code> é o script Python que simula o envio dos dados.<br>
 
<code>docker-compose.yml</code> é o arquivo de configuração do para a criação dos containes Docker.<br>
 
<code>ansible.yml</code> é o arquivo de instruçoes para configuração do anbiente utilisando o Ansible.<br>
 
 
<hr>
 
<br>
 
<h5><b>Uso: </b></h5>
 
<p>Após a instalação do Ansible, execute o seguinte comando no diretório do programa:</p>
 
<code> <b>ansible-playbook ansible.yml --ask-become-pass</b> </code>
 
<br>
 
<h5><b>Conferir funcionamento:</b></h5>
 
<p>Execute o comando <code>sudo docker ps -a</code>, ele mostrara o estado dos containes criados. Os conteneres de nome plantaDC, nodeRed, grafana, mosquitto e InfluxDB devem ter cido criados e estar ligados.</p>
 
<br>
 
<h5><b>Simular sensores:</b></h5>
 
<p>Para simular a atividade de sensores execute o arquivo <code>sensores_todos.py</code> rodando: </p>

<code>python3 sensores_todos.py</code>
 
 
