# Save this in keylogger_tool/utils/utils.py
import logging

def setup_logging():
    # Setting up logging for debugging or future improvements
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    logging.info("Keylogger Tool Initialized.")
