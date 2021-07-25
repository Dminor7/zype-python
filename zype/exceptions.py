class ResponseProcessException(Exception):
    def __init__(self, zype_exception, data, *args, **kwargs):
        self.zype_exception = zype_exception
        self.data = data
        super(ResponseProcessException, self).__init__(*args, **kwargs)


class ZypeException(Exception):
    def __init__(self, message, client):
        self.status_code = None
        self.client = client
        if client is not None:
            self.status_code = client().status_code

        if not message:
            message = "response status code: {}".format(self.status_code)
        super(ZypeException, self).__init__(message)


class ClientError(ZypeException):
    def __init__(self, message="", client=None):
        super(ClientError, self).__init__(message, client=client)


class ServerError(ZypeException):
    def __init__(self, message="", client=None):
        super(ServerError, self).__init__(message, client=client)
