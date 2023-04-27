import socket
import argparse
import threading
import json

class ClientThread(threading.Thread):
    def __init__(self, urls, num_threads, top_k):
        threading.Thread.__init__(self)
        self.urls = urls
        self.num_threads = num_threads
        self.top_k = top_k

    def run(self):
        for url in self.urls:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("localhost", 8888))
                s.sendall(url.encode('utf-8'))
                result = s.recv(1024).decode('utf-8')
                result = json.loads(result)
                print(f"{url}: {result}")

class Client:
    def __init__(self, num_threads, top_k, urls_file):
        self.num_threads = num_threads
        self.top_k = top_k
        self.urls_file = urls_file
    
    def run(self):
        # читаем URL'ы из файла
        with open(self.urls_file) as f:
            urls = f.readlines()
        urls = [url.strip() for url in urls]

        # запускаем потоки
        threads = []
        for i in range(self.num_threads):
            thread = ClientThread(urls[i::self.num_threads], self.num_threads, self.top_k)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # ждем завершения всех потоков
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="number of threads")
    parser.add_argument("urls_file", type=str, help="path to file with URLs")
    parser.add_argument("-k", "--top_k", type=int, default=10, help="top K words")
    args = parser.parse_args()

    client = Client(args.num_threads, args.top_k, args.urls_file)
    client.run()
