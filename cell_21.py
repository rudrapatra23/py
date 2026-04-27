import threading
import time
import random

lock = threading.Lock()
buffer = []
production_complete = False

def producer():
    global buffer, production_complete
    for _ in range(5):
        val = random.randint(1, 100)
        with lock:
            buffer.append(val)
            print(f"Produced: {val}")
        time.sleep(0.1)
    production_complete = True

def consumer():
    global buffer
    while True:
        with lock:
            if buffer:
                print(f"Consumed: {buffer.pop(0)}")
            elif production_complete:
                break
        time.sleep(0.1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Buffer empty. Process complete.")