docker exec -it mocommender_kafka_1 kafka-console-producer.sh \
	--bootstrap-server localhost:9092 \
	--topic mocommender_topic
