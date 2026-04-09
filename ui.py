import tkinter as tk
from logger import start_logging, stop_logging, get_key_counts
from analyzer import show_stats, plot_graph

def start():
    start_logging()
    status_label.config(text="Status: Logging Started")

def stop():
    stop_logging()
    status_label.config(text="Status: Logging Stopped")

def stats():
    kc = get_key_counts()
    show_stats(kc)

def graph():
    kc = get_key_counts()
    plot_graph(kc)

# Create window
root = tk.Tk()
root.title("Keystroke Analyzer")
root.geometry("300x250")

tk.Button(root, text="Start Logging", command=start).pack(pady=10)
tk.Button(root, text="Stop Logging", command=stop).pack(pady=10)
tk.Button(root, text="Show Stats", command=stats).pack(pady=10)
tk.Button(root, text="Show Graph", command=graph).pack(pady=10)

status_label = tk.Label(root, text="Status: Idle")
status_label.pack(pady=10)