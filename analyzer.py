import matplotlib
matplotlib.use('TkAgg')  # Fix for GUI backend

import matplotlib.pyplot as plt

def show_stats(key_count):
    print("\n--- Keystroke Stats ---")
    for key, count in key_count.items():
        print(f"{key}: {count}")

def plot_graph(key_count):
    if not key_count:
        print("No data to display!")
        return

    keys = list(key_count.keys())
    counts = list(key_count.values())

    plt.figure()
    plt.bar(keys, counts)
    plt.xlabel("Keys")
    plt.ylabel("Frequency")
    plt.title("Keystroke Analysis")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()