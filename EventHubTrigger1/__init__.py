import logging

import azure.functions as func
from azure.eventhub import EventHubProducerClient, EventData
import json

producer = EventHubProducerClient.from_connection_string(
    conn_str="<eventhub-connection-string>",
    eventhub_name="<eventhub-name-2>"
)

def main(event: func.EventHubEvent):

    bs = event[0].get_body().decode("utf-8")
    logging.info(type(bs))

    json_obj = json.loads(bs)

    s = json.dumps(json_obj)

    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(s))
    producer.send_batch(event_data_batch)
