# Kafka_stock_market
Create a Kafka system to load real time stock market data into s3, catalogue with AWS glue and search using AWS Athena

The producer for the Kafka is mimicked using a python sampling system from a raw data.
Kafka topic, producers and consumer is created.
The consumer loads the data into AWS s3 as JSON files. 
AWS Glue crawler is used to create a data catalogue for the JSON files.
AWS Athena is used to search within the output using query scripts.
