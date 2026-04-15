import psutil
import threading
import time

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"


def block_website(site):
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()

        if site not in content:
            file.write(f"{REDIRECT_IP} {site}\n")
            file.write(f"{REDIRECT_IP} www.{site}\n")


def unblock_website(site):
    with open(HOSTS_PATH, "r") as file:
        lines = file.readlines()

    with open(HOSTS_PATH, "w") as file:
        for line in lines:
            if site not in line:
                file.write(line)


def block_with_timer(site, duration):
    def task():
        block_website(site)
        print(f"{site} blocked")

        time.sleep(duration)

        unblock_website(site)
        print(f"{site} unblocked")

    threading.Thread(target=task).start()


def block_app_with_timer(app_name, duration):
    def task():
        end_time = time.time() + duration

        while time.time() < end_time:
            for process in psutil.process_iter(['name']):
                try:
                    if process.info['name'] and app_name.lower() in process.info['name'].lower():
                        process.kill()
                except:
                    pass

            time.sleep(0.5)

        print(f"{app_name} is now unblocked")

    threading.Thread(target=task).start()