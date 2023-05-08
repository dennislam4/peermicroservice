import zmq
import time
from collections import defaultdict
import datetime


def format_timestamp(timestamp):
    """
    Uses month name, day, year, hour:minute AM/PM format to mark timestamps of messages.
    """
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%B %d, %Y %I:%M %p")


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    messages = defaultdict(list)
    print("The server is up and running!")
    # Main server loop
    while True:
        # Receive a JSON request from a client
        request = socket.recv_json()
        # Get the action (user input) and client_id from the request
        action = request['action']
        client_id = request['client_id']

        # If the action is 'send', store the message and send a response
        if action == 'send':
            message = request['message']
            timestamp = time.time()
            formatted_timestamp = format_timestamp(timestamp)
            messages[client_id].append((timestamp, message))
            socket.send_string(f"Message received at {formatted_timestamp}")

        # If the action is 'get', send the messages for the client
        elif action == 'get':
            user_messages = messages[client_id]
            socket.send_json(user_messages)


if __name__ == "__main__":
    main()
