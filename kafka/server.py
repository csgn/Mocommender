import os
import json
import uuid

from flask import Flask, request
from flask_cors import CORS
from kafka import KafkaProducer

kafka_topic = os.environ.get('KAFKA_APP_TOPIC', 'mocommender_topic')
kafka_host =  os.environ.get('KAFKA_HOSTNAME', 'localhost')
kafka_port = os.environ.get('KAFKA_PORT', 9093)

kafka_bootstrap_servers = f'{kafka_host}:{kafka_port}'

producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v,
                                                               indent=4,
                                                               default=str) \
                                                        .encode('utf-8'))

app = Flask(__name__)

CORS(app)


@app.route('/send', methods=['POST'])
def index():
    
    body = request.json 
    print(kafka_topic, kafka_bootstrap_servers, body)
    key = str(uuid.uuid4())
    producer.send(topic=kafka_topic,
                  value=body,
                  key=bytes(key, encoding='utf-8'))
    
    return "SENT"

if __name__ == '__main__':
    app.run()
