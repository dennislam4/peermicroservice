# Assignment 8: Microservice Implementation (Milestone #2)

This microservice will allow users to send and receive messages using ZeroMQ. Clients can send messages and request to fetch their messages from the server. All messages sent and received have intergrated timestamps which can be useful for your personal project.

## Get Started
1. Download the client.py and server.py files
2. Install any neccessary packages (ZeroMQ)
3. Run the server.py file and then the client.py file in order, through seperate terminals
```python
python server.py
python client.py
```

## Requesting Data from the Microservice
To send a message using the client, follow these steps:
1. Run the client script.
2. When prompted, enter 'send'.
3. Enter your message.

Example:
```python
Enter 'send' to send a message or 'get' to get your messages:
send
Enter your message: Hello, world!
Server response: Message received at May 08, 2023 12:34
```

## Receiving Data from the Microservice
To receive your messages from the server, follow these steps:
1. Run the client script.
2. When prompted, enter 'get'.

Example:
```python
Enter 'send' to send a message or 'get' to get your messages:
get
[May 08, 2023 12:34] Hello, world!
[May 08, 2023 12:35] Another message!
```
### UML sequence diagram:
![UMLsequence](https://user-images.githubusercontent.com/107871794/236950638-f1f0afcb-9e58-44ec-9ab1-da4ded56bdf7.png)


