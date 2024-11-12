import websocket
import json
import time


class WebSocket:
    ws: websocket.WebSocketApp
    socket: str
    socket_data: list
    init_time: float
    msg_time: float

    def __init__(self, socket):
        self.socket = socket
        self.init_time = time.time()
        self.socket_data = []
        self.__start_websocket(self.socket)

    def __start_websocket(self, socket):
        self.ws = websocket.WebSocketApp(socket,
                                    on_open=self.__on_open,
                                    on_message=self.__on_message,
                                    on_error=self.__on_error,
                                    on_close=self.__on_close)
        self.ws.run_forever(ping_timeout=30)

    def __on_open(self, ws):
        print("--- opened ---")

    def __on_message(self, ws, message):
        self.msg_time = time.time()
        time_delta = self.msg_time - self.init_time
        msg = json.loads(message)
        if 'action' in msg and msg['action'] == 'insert':
            self.socket_data.append(msg)
            ws.close()
        if time_delta > 10:
            ws.close()

    def __on_error(self, error):
        print(error)

    def __on_close(self, ws):
        print("--- closed ---")

    def get_socket_data(self):
        if not self.socket_data:
            return False
        else:
            return self.socket_data
