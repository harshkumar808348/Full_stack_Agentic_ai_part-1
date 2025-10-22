import threading
import requests

import time

def download(url):
    print(f"Starting download form {url}")
    res = requests.get(url)
    print(f"Finised downloading  from {url}, size:{len(res.content)} bytes")
    
url = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for urls in url:
    t = threading.Thread(target=download , args=(urls,))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
end = time.time()

print(f"All the download done in {end -start:.2f} seconds")