import socket
import threading
import json
import argparse
from collections import Counter
import requests
from bs4 import BeautifulSoup
import re
from queue import Queue


class Worker(threading.Thread):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.daemon = True
        self.start()

    def run(self):
        while True:
            client_data = self.master.queue.get()
            if client_data is None:
                break
            client, k = client_data
            try:
                response = self.process_request(client, k)
                client.send(json.dumps(response).encode("utf-8"))
                self.master.queue.task_done()
                with self.master.lock:
                    self.master.urls_processed += 1
                    print(f"URLs processed: {self.master.urls_processed}")
            except Exception as e:
                print(f"Error in worker: {e}")
            finally:
                client.close()

    def process_request(self, client, k):
        url = client.recv(1024).decode("utf-8")
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            words = re.findall(r'\w+', soup.get_text().lower())
            top_k_words = dict(Counter(words).most_common(k))
            return top_k_words
        except Exception as e:
            return {"error": str(e)}


class Master:
    def __init__(self, num_workers, k):
        self.queue = Queue()
        self.lock = threading.Lock()
        self.urls_processed = 0
        self.host = "0.0.0.0"
        self.port = 9999
        self.workers = [Worker(self) for _ in range(num_workers)]
        self.k = k

    def serve(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server started on port {self.port}")
            try:
                while True:
                    client, addr = s.accept()
                    self.queue.put((client, self.k))
            except KeyboardInterrupt:
                pass
            finally:
                self.queue.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workers", type=int, default=4, help="Number of workers")
    parser.add_argument("-k", "--top_k", type=int, default=5, help="Top K frequent words")
    args = parser.parse_args()

    master = Master(args.workers, args.top_k)
    master.serve()
