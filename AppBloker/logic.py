import psutil
import threading
import time


HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"


def block_website(site):

   with open(HOSTS_PATH , "r+") as file:
        content = file.read()

        if site not in content:
            file.write(f"{REDIRECT_IP} {site}\n")
            file.write(f"{REDIRECT_IP} www.{site}\n")


## what the fuck

def unblock_website(site):
    with open(HOSTS_PATH ,"r") as file:
        lines = file.readlines()

    with open (HOSTS_PATH  , "w") as file:
        for line in lines:
             if site not in line:
                 file.write(line)       


def block_with_timer(site ,duration):
    def task():
        block_website(site)
        print(f"{site} blocked")


        time.sleep(duration)  
        

        unblock_website(site)
        print(f"{site} unblocked")

    threading.Thread(target=task).start()                   