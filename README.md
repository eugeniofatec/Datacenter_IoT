<h3 align="center">Configurações</h3>

<p>Em ambiente Linux (Mint, Ubuntu), o arquivo de configuração do Mosquitto deve estar em <code>/etc/mosquitto/</code>. O arquivo <b>mosquitto.conf</b> obriga que as conexões usem senha e usuário, por isso ele aponta para o arquivo <code>senhas.txt</code>, que deve estar na mesma pasta que o arquivo de configuração.<br>

<br>Para criar um arquivo de senha com um usuário, dentro da pasta onde está o arquivo de configuração do Mosquitto, execute:<br>
<code>$ mosquitto_passwd -c senhas.txt Nome_do_usuario</code><br>
<br>
Vai ser solicitado uma senha para o usuário informado no comando acima.
