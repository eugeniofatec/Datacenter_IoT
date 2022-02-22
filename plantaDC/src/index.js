const express = require("express");
const influxConnection = require('./controller/connection');
const app = express();

app.get("/", (req, res) => res.sendFile(__dirname + "/view/home.html"))

app.get("/planta/DC", (req, res) => res.sendFile(__dirname + "/view/plantaDC.html"))

app.get("/lerdados", (req, res) => {

    influxConnection.query(
        "select PM, Temperatura, Umidade from Sensores where time > now() - 5s"
    ).then(
        result => res.status(200).json(result)
    ).catch(
        error => res.status(500).json({ error })
    );
})

app.get("/erro/:erroJson", (req, res) => res.sendFile(__dirname + "/view/erro_bd.html"))

app.use((req, res) => res.status(404).sendFile(__dirname + "/view/404.html"));

app.listen(5000, () => {
    console.log("Servidor rodando");
});