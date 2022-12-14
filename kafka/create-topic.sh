docker exec -it mocommender_kafka_1 kafka-topics.sh \
	--create \
	--topic mocommender_topic \
	--replication-factor 1 \
	--partitions 1 \
	--bootstrap-server localhost:9092

