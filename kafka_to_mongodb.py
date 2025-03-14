# kafka_to_mongodb.py
from kafka import KafkaConsumer
from pymongo import MongoClient
import json

def main():
    # Set up Kafka consumer to read from topic 'log_topic'
    consumer = KafkaConsumer(
        'log_topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs_db']
    collection = db['log_entries']

    for message in consumer:
        log_entry = message.value
        # Basic cleaning: ensure message text is lowercase and trimmed
        log_entry['log_message'] = log_entry.get('log_message', '').lower().strip()
        collection.insert_one(log_entry)
        print("Inserted log entry:", log_entry)

if __name__ == "__main__":
    main()
