from azure.eventhub import EventHubProducerClient, EventData
import json
import time

f = open("small.json")
s = json.load(f)
json_string = json.dumps(s)

producer = EventHubProducerClient.from_connection_string(
    conn_str="<eventhub-connection-string>",
    eventhub_name="<eventhub-name-1>"
)

def send_event(producer):
    producer.send_event(EventData(json_string))

start_time = time.time()
with producer:
    send_event(producer)


print("Send messages in {} seconds.".format(time.time() - start_time))