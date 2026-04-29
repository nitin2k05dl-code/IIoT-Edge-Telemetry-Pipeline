# Industrial Edge Telemetry Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![Node-RED](https://img.shields.io/badge/Node--RED-8F0000?style=for-the-badge&logo=node-red&logoColor=white)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

## Objective
An end-to-end edge computing architecture designed to extract, route, and visualize high-frequency machine telemetry. This serves as the foundational data infrastructure required for IIoT Digital Twin condition monitoring, built in preparation for the CREDIT project at TU Chemnitz.

## System Architecture

```mermaid
graph LR
    A[Python CNC Simulation] -->|JSON Payload| B[Mosquitto MQTT Broker]
    B -->|Topic Routing| C[Node-RED Edge Processing]
    C -->|Data Structuring| D[(InfluxDB Time-Series Database)]
    D -->|Flux Query Downsampling| E[Grafana Dashboard]
