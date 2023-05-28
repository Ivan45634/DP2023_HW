import unittest
from unittest.mock import patch, MagicMock
from client import ClientThread


class TestClientThread(unittest.TestCase):
    def test_run(self):
        url = "http://test.com"
        client_thread = ClientThread(url)

        with patch('socket.socket') as mock_socket, patch("builtins.print") as mock_print:
            mock_socket_instance = MagicMock()
            mock_socket.return_value.__enter__.return_value = mock_socket_instance
            mock_socket_instance.recv.return_value = '{"example": 3, "test": 2}'.encode("utf-8")

            client_thread.run()

            mock_socket_instance.connect.assert_called_once()
            mock_socket_instance.sendall.assert_called_once_with(url.encode("utf-8"))
            mock_print.assert_called_once_with(f"{url}: {{'example': 3, 'test': 2}}")

    def test_run_invalid_url(self):
        url = "invalid_url"
        client_thread = ClientThread(url)

        with patch('socket.socket') as mock_socket, patch("builtins.print") as mock_print:
            mock_socket_instance = MagicMock()
            mock_socket.return_value.__enter__.return_value = mock_socket_instance
            mock_socket_instance.recv.return_value = '{"error": "Invalid URL"}'.encode("utf-8")

            client_thread.run()

            mock_socket_instance.connect.assert_called_once()
            mock_socket_instance.sendall.assert_called_once_with(url.encode("utf-8"))
            mock_print.assert_called_once_with(f"{url}: {{'error': 'Invalid URL'}}")


if __name__ == "__main__":
    unittest.main()
