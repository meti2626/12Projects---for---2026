### python threading example

import threading
import time


def crawl(link , delay = 3):

   print(f"crawl started for {link}") 
   time.sleep(delay)
   print(f"crawl finished for {link}")

links =   [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

threads = []

for link in links:

    t = threading.Thread(target = crawl , args =(link ,), kwargs= {"delay" : 2} )
    threads.append(t)


for t in threads:
   t.start()

for t in threads:
   t.join()   