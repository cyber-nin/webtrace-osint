import time

def run_scheduler(task, interval=60):
    while True:
        task()
        time.sleep(interval)
