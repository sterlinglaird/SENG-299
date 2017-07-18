import json
from socket import socket

class Command:
    def __init__(self, data=None):
        """
        The class that contains command related functionality.
        """

        # Initialize the command based on data provided
        if data is not None:
            data = json.loads(data)
            self.type = data['type']
            self.body = data['body']
            self.creator = data['creator']
            self.specificChatroom = data['specificChatroom']
        else:
            self.type = None
            self.body = None
            self.creator = None
            self.specificChatroom = None

    def init_send_message(self, message: str, specificChatroom: str):
        """
        Initializes the message command.
        """

        self.type = 'message'
        self.body = message
        self.specificChatroom = specificChatroom

    def init_connect(self, alias: str):
        """
        Initializes the connect command.
        """

        self.type = 'connect'
        self.body = alias

    def init_disconnect(self):
        """
        Initializes the disconnect command.
        """

        self.type = 'disconnect'
        self.body = None

    def init_join_chatroom(self, chatroom: str):
        """
        Initializes the join chatroom command.
        """

        self.type = 'join_chatroom'
        self.body = chatroom

    def init_create_chatroom(self, chatroom: str):
        """
        Initializes the create chatroom command.
        """

        self.type = 'create_chatroom'
        self.body = chatroom

    def init_delete_chatroom(self, chatroom: str):
        """
        Initializes the delete chatroom command.
        """

        self.type = 'delete_chatroom'
        self.body = chatroom

    def init_error(self, message):
        """
        Initializes the delete chatroom command.
        """

        self.type = 'error'
        self.body = message

    def send(self, sock: socket):
        """
        Sends the command using the provided socket.
        """

        data = json.dumps({'type': self.type, 'creator': self.creator, 'specificChatroom': self.specificChatroom, 'body': self.body})
        sock.send(data.encode(encoding='UTF-8'))