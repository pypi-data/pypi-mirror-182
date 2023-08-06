#!/bin/python

class MainError(Exception):
    pass

class NotREGISTERED(IOError):
    ...

class InvalidInput(IOError):
    ...

class TooREQUESTS(IOError):
    ...

class InvalidAUTH(IOError):
    ...

class ConnectError(BaseException):
    ...

class ClientError(Exception):
    ...

class ServerError(
    Exception
    ):
    ...

class Errors(
    Exception
    ):
    
    def MadeError(status: str, det: str) -> (bool or ...):

        if status.upper() == 'ERROR_GENERIC' or status.upper() == 'ERROR_ACTION':
            if 'NOT_REGISTERED' in det.upper():
                raise NotREGISTERED('session key not found; please find your key in web.rubika.ir and try again.')
            elif 'INVALID_INPUT' in det.upper():
                raise InvalidInput('your inserts is not true; try again.')
            elif 'TOO_REQUESTS' in det.upper():
                raise TooREQUESTS('sorry; method has been limited, please try again later.')
            elif 'INVALID_AUTH' in det.upper():
                raise InvalidAUTH('sorry; server error or please check method arguments and try again.')
            else:
                return True
        else:
            return True

class ClientConnectorError(object):
    
    @classmethod
    def __init__(cls, **kwargs: object) -> (...):
        cls.set_error: ConnectError = kwargs.get('error')
        cls.name: str = kwargs.get('name')
        super().__init__(cls.name, cls.set_error)
        
    @property
    def raises(cls) -> (Exception):
        raise cls.set_error(f'this error for {cls.name}')
    
    @property
    def returns(cls) -> (str):
        return 'this error for %s please fixed and try again.' %  cls.name

