import socket
import threading
import json
import argparse


class ClientThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url.strip()
        self.host = "127.0.0.1"
        self.port = 9999

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(self.url.encode("utf-8"))
                data = s.recv(1024)
                decoded_data = json.loads(data.decode("utf-8"))
                print(f"{self.url}: {decoded_data}")
        except Exception as e:
            print(f"Error in client thread for {self.url}: {e}")


def process_urls(file_name, num_threads):
    with open(file_name, "r") as f:
        urls = f.readlines()

    for i in range(0, len(urls), num_threads):
        threads = [ClientThread(url) for url in urls[i:i+num_threads]]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads")
    parser.add_argument("file", help="File with URLs")
    args = parser.parse_args()

    process_urls(args.file, args.threads)
