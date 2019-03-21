class ConnectionException(Exception):
    def __init__(self, host, port):
        Exception.__init__(self, host, port)
        self.message = f'Cannot connect to {host}:{port}.'
