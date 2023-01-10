import time
from worker import worker

def init_worker():
    worker.perform_check()
    time.sleep(1)
    init_worker()



if __name__ == "__main__":
    init_worker()

