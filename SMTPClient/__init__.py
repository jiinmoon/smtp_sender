from socket import *
from SMTPClient.exceptions import ConnectionException

class Client():
    def __init__(self, serverAddr='', serverPort=25):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverAddr = serverAddr
        self.serverPort = serverPort

        try:
            self.serverSocket.connect((serverAddr, serverPort))
            response = self.serverSocket.recv(1024).decode()
            print(response)
            self.serverSocket.send('HELO ALICE\r\n'.encode())
            response = self.serverSocket.recv(1024)
            print(response.decode('utf-8'))
        except (AttributeError, gaierror):
            raise ConnectionException(serverAddr, serverPort)

    def sendCommands(self, commands=[]):
        try:
            for command in commands:
                print(command)
                self.serverSocket.send(command.encode())
                response = self.serverSocket.recv(1024)
                print(response.decode('utf-8'))
        except:
            print('error in sending commands: \n\t{}'.format(commands))

    def setFromTo(self, mailFrom='', mailTo=''):
        self.mailFrom = mailFrom
        self.mailTo = mailTo
        commands=[
                'MAIL FROM:{}\r\n'.format(self.mailFrom),
                'RCPT TO:{}\r\n'.format(self.mailTo)
                ]
        self.sendCommands(commands)

    def setMsg(self, msg=''):
        self.msg = msg
        print('sending {}'.format(self.msg))

        commands=[
                'DATA\r\n',
                '{}\r\n.\r\n'.format(self.msg),
        ]
        self.sendCommands(commands)

    def takeDown(self):
        commands=[
            'QUIT\r\n'
        ]
        self.sendCommands(commands)
        self.serverSocket.close()

