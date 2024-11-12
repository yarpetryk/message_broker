from helpers.websocket import WebSocket

class TestWebsocket:

    def test_websocket(self):
        websocket_listener = WebSocket(socket='wss://www.bitmex.com/realtime?subscribe=trade:XBTUSD')
        result = websocket_listener.get_socket_data()
        assert len(result) > 0
        print(result)
        print(len(result))


