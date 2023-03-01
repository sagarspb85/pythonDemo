import paho.mqtt.client as mqtt

# Define MQTT broker settings
broker_address = "wss://pmkbroker.hkapl.in:80/ws"
port = 80
username = "cmpb_live:mhpmkusum"
password = "pmkusum@2026"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("CMP-B/district/27")

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))

def on_publish(client, userdata, mid):
    print("Message published")

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))

# Create MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Connect to MQTT broker
client.connect(broker_address, port)

# Start the network loop
client.loop_start()

# Publish a message
client.publish("test", "Hello, World!")

# Disconnect from MQTT broker
client.disconnect()

# Stop the network loop
client.loop_stop()
