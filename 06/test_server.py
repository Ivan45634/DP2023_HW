import unittest
from unittest.mock import patch, MagicMock
from server import Worker, Master


class TestWorker(unittest.TestCase):
    def setUp(self):
        self.master = Master(1, 3)
        self.worker = Worker(self.master)

    @patch("requests.get")
    @patch("server.BeautifulSoup")
    def test_process_request(self, mock_soup, mock_get):
        mock_response = MagicMock()
        mock_response.text = "<html><body>Test test example example example</body></html>"
        mock_get.return_value = mock_response

        mock_bs_instance = MagicMock()
        mock_bs_instance.get_text.return_value = "Test test example example example"
        mock_soup.return_value = mock_bs_instance

        client = MagicMock()
        client.recv.return_value = "http://test.com".encode("utf-8")

        expected = {"example": 3, "test": 2}
        result = self.worker.process_request(client, 3)

        self.assertEqual(result, expected)

    def test_process_request_invalid_url(self):
        client = MagicMock()
        client.recv.return_value = "invalid_url".encode("utf-8")

        result = self.worker.process_request(client, 3)

        self.assertIn("error", result)


class TestMaster(unittest.TestCase):
    @patch("socket.socket")
    @patch("socket.AF_INET")
    @patch("socket.SOCK_STREAM")
    def test_master_init(self, mock_af_inet, mock_sock_stream, mock_socket):
        master = Master(2, 3)

        self.assertEqual(len(master.workers), 2)


if __name__ == "__main__":
    unittest.main()
