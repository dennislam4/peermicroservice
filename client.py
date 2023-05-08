import datetime
import random
import zmq


def format_timestamp(timestamp):
    """
    Uses month name, day, year, hour:minute AM/PM format to mark timestamps of messages.
    """
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%B %d, %Y %I:%M %p")


def main():
    # Generates a random client ID. This could be replaced with a user that you implement in your app
    client_id = f"Client{random.randint(1000, 9999)}"
    print(f"Your client ID is: {client_id}")

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        print("Enter 'send' to send a message or 'get' to get your messages:")
        action = input().lower()

        # If the action is 'send', send a message to the server
        if action == 'send':
            message = input("Enter your message: ")
            request = {'action': 'send', 'client_id': client_id, 'message': message}
            socket.send_json(request)
            response = socket.recv_string()
            print(f"Server response: {response}")

        # If the action is 'get', request messages from the server
        elif action == 'get':
            request = {'action': 'get', 'client_id': client_id}
            socket.send_json(request)
            messages = socket.recv_json()

            # If no messages were found, displays error message
            if not messages:
                print("No messages were found.")
            else:
                # Print received messages with formatted timestamps
                for timestamp, message in messages:
                    print(f"[{format_timestamp(timestamp)}] {message}")
        # If the input is invalid, display an error message
        else:
            print("Invalid input. Please enter 'send' or 'get'.")


if __name__ == "__main__":
    main()
