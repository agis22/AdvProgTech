import time
from paho.mqtt import client as mqtt_client

# Ορίστε τις μεταβλητές broker, port, topic, client_id.
mqtt_broker = 'test.mosquitto.org'
mqtt_port = 1883
mqtt_topic = "grupatras/lab/1072803"

# Generate a Client ID with the publish prefix.
client_id = f'publish-999'

# Connect to MQTT broker.
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(mqtt_broker, mqtt_port)
    return client

def main():
    client = connect_mqtt()
    # Start publishing
    client.loop_start()
    # Publish message
    time.sleep(1)
    msg = "You have " + str(i+1) + " messages"
    result = client.publish(mqtt_topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic: {mqtt_topic}")
    else:
        print(f"Failed to send message to topic: {mqtt_topic}")
    # Stop publishing
    client.loop_stop()


if __name__ == '__main__':
    main()
