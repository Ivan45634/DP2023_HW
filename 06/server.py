import socket
import json
import threading
from queue import Queue

class WorkerThread(threading.Thread):
    def __init__(self, worker_id, queue):
        threading.Thread.__init__(self)
        self.worker_id = worker_id
        self.queue = queue

    def run(self):
        while True:
            client_socket, client_address = self.queue.get()
            url = client_socket.recv(1024).decode('utf-8')
            print(f"Worker {self.worker_id}: starting {url}...")
            # здесь ваш код обработки запроса
            # например, обкачка страницы и подсчет частоты слов
            result = {"word1": 10, "word2": 5}
            print(f"Worker {self.worker_id}: finished {url}.")
            client_socket.sendall(json.dumps(result).encode('utf-8'))
            client_socket.close()
            self.queue.task_done()

class Server:
    def __init__(self, host, port, num_workers, top_k):
        self.host = host
        self.port = port
        self.num_workers = num_workers
        self.top_k = top_k
    
    def run(self):
        self.queue = Queue()
        for i in range(self.num_workers):
            worker = WorkerThread(i, self.queue)
            worker.daemon = True
            worker.start()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen()

            print(f"Server is listening on {self.host}:{self.port}")

            while True:
                client_socket, client_address = s.accept()
                print(f"Received connection from {client_address}")
                self.queue.put((client_socket, client_address))


if __name__ == "__main__":
    server = Server("localhost", 8888, 10, 7)
    server.run()
