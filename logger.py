from pynput.keyboard import Listener
from datetime import datetime
import threading

key_count = {}
listener = None
logging_active = False

def on_press(key):
    global key_count, logging_active

    if not logging_active:
        return

    try:
        key = key.char  # for normal keys
    except AttributeError:
        key = str(key)  # for special keys

    print("Pressed:", key)  # ✅ DEBUG (important)

    key_count[key] = key_count.get(key, 0) + 1

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"{time} - {key}\n")


def run_listener():
    with Listener(on_press=on_press) as l:
        l.join()


def start_logging():
    global logging_active

    logging_active = True

    # Start listener in separate thread
    t = threading.Thread(target=run_listener)
    t.daemon = True
    t.start()


def stop_logging():
    global logging_active
    logging_active = False


def get_key_counts():
    return key_count