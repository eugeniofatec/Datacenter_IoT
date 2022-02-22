
echo "\
APP_PATH=$PWD
" > docker.env 

sudo docker-compose --env-file "docker.env"  -f "docker-compose.yml" up -d
