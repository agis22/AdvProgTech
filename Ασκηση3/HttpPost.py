
import json
import paho.mqtt.client as mqtt

# MQTT broker settings
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883
mqtt_topic = "grupatras/lab/1072803"

# Initialize MQTT client
mqtt_client = mqtt.Client()

# Connect to the MQTT broker
mqtt_client.connect(mqtt_broker, mqtt_port)

# HTTP POST data
post_data = {
    "text": "Hello World!",
    "id": 1
}

# Convert HTTP POST request to a string
http_post_request = json.dumps(post_data)  # Convert to JSON string

# Publish the MQTT message with the HTTP POST request
mqtt_client.publish(mqtt_topic, http_post_request)
print("Published: " + http_post_request)

# Disconnect from the MQTT broker
mqtt_client.disconnect()