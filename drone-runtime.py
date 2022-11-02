# Import the built-in socket and time modules
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Let's be explicit and bind to a local port on our machine where Tello can send messages
sock.bind(('', 9000))

# Function to send messages to Tello
def send(message):
    try:
        sock.sendto(message.encode(), tello_address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

# Function that listens for messages from Tello and prints them to the screen
def receive():
    try:
        response, ip_address = sock.recvfrom(128)
        print("Received message: " + response.decode(encoding='utf-8') + " from Tello with IP: " + str(ip_address))
    except Exception as e:
        print("Error receiving: " + str(e))


# Send Tello into command mode
send("command")

# Receive response from Tello
receive()

# Delay 3 seconds before we send the next command
time.sleep(3)

# Ask Tello about battery status
send("battery?")

# Receive battery response from Tello
receive()


## Mission 1
# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
box_leg_distance = 100

# Yaw 90 degrees
yaw_angle = 90

# Yaw clockwise (right)
yaw_direction = "cw"

# Put Tello into command mode
send("command", 3)

# Send the takeoff command
send("takeoff", 5)

# Fly forward
send("forward " + str(box_leg_distance), 4)

# Yaw right
send("cw " + str(yaw_angle), 3)

# Fly forward
send("forward " + str(box_leg_distance), 4)

# Yaw right
send("cw " + str(yaw_angle), 3)

# Fly forward
send("forward " + str(box_leg_distance), 4)

# Yaw right
send("cw " + str(yaw_angle), 3)

# Fly forward
send("forward " + str(box_leg_distance), 4)

# Yaw right
send("cw " + str(yaw_angle), 3)

# Land
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock.close()