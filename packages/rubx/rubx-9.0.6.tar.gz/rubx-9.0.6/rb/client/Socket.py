#!/bin/python

from json import dumps, loads

from ..crypto import Encryption


class WebSocket(
    object,
    ):

    data: dict = {
        'error'     :   [],
        'message'  :   []
        }

    def __init__(
        self,
        session_id
        ) -> ...:
        self.auth: str = session_id
        self.enc: Encryption = Encryption(
            session_id
            )

    def __enter__(
        self
        ) -> ...:
        return self

    def __exit__(
        self,
        *args,
        **kwargs
        ) -> ...:
        pass

    def on_open(self, ws, api_version='5') -> None :
        def handShake(*args):
            ws.send(
                dumps(
                    {
                        'api_version'   :   api_version,
                        'auth'          :   self.auth,
                        'method'        :   'handShake'
                        }
                    )
                )
        import _thread
        _thread.start_new_thread(
            handShake,
            ()
            )

    def on_error(
        self,
        error
        ) -> ...:
        WebSocket.data[
            'error'
            ].append(
                error
                )

    def on_message(
        self,
        message
        ) -> ...:
        try:

            parsedMessage = loads(message)
            WebSocket.data[
                'messages'
                ].append(
                    {
                        'type'  :   parsedMessage[
                            "type"
                            ],
                        'data'  :   loads(
                            self.enc.decrypt(
                                parsedMessage[
                                    "data_enc"
                                    ]
                                )
                            )
                        }
                    )

        except KeyError:
            pass
    
    def on_close(
        self,
        code,
        msg
        ) -> ...:

        return {
            'code': code,
            'message': msg
            }

    def handle(
        self,
        OnOpen=None,
        OnError=None,
        OnMessage=None,
        OnClose=None,
        forEver=True
        ) -> ...:
        from websocket import WebSocketApp
        ws: WebSocketApp = WebSocketApp (
            'wss://jsocket3.iranlms.ir:80',
            on_open=OnOpen or WebSocket(
                self.auth
                ).on_open,
            on_message=OnMessage or WebSocket(
                self.auth
                ).on_message,
            on_error=OnError or WebSocket(
                self.auth
                ).on_error,
            on_close=OnClose or WebSocket(
                self.auth
                ).on_close
            )

        if forEver:
            ws.run_forever()