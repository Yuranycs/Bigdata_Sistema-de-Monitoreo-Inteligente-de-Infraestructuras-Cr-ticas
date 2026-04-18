nano ejercicio1_kafka_producer.py

import time, json, random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    data = {
        "sensor_id": f"DC_SENSOR_{random.randint(1, 5)}",
        "temperatura": random.uniform(20.0, 40.0),
        "humedad": random.uniform(30.0, 60.0),
        "timestamp": time.time()
    }
    producer.send('sensor_data', json.dumps(data).encode('utf-8'))
    print(f"Enviado: {data}")
    time.sleep(1)

