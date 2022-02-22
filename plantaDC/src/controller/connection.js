const Influx = require('influx');

const influxConnection = new Influx.InfluxDB(`http://influxdb:8086/Monitoramento`)

module.exports = influxConnection;