#!/usr/bin/env python3
"""
Smore: Bitcoin Wallet Brute-force Tool
Main entry point for the application
"""
import os
import sys
import logging
import time
import threading
from pathlib import Path
import customtkinter as ctk

# Fix path to make imports work
current_dir = os.path.abspath(os.path.dirname(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Ensure logs directory exists
logs_dir = Path(current_dir) / "smore" / "logs"
logs_dir.mkdir(exist_ok=True)

# Configure root logger with a buffer handler
class BufferHandler(logging.Handler):
    def __init__(self, capacity=1000):
        super().__init__()
        self.capacity = capacity
        self.buffer = []
        
    def emit(self, record):
        self.buffer.append(self.format(record))
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)
            
    def get_logs(self):
        return self.buffer

# Create buffer handler for storing logs until app is ready
buffer_handler = BufferHandler()
buffer_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(str(logs_dir / "smore.log")),
        logging.StreamHandler(),
        buffer_handler
    ]
)

# Get logger
logger = logging.getLogger(__name__)

def load_dependencies():
    """
    Pre-load dependencies to avoid freezing during app startup.
    Returns success status.
    """
    try:
        # Try to import key dependencies
        import numpy
        import customtkinter
        import requests
        import threading
        import ecdsa
        import base58
        
        # Preload bitcoin wallet implementation
        from smore.utils.crypto import BitcoinWallet
        wallet = BitcoinWallet()
        
        # Pre-initialize GPU detection in background
        from smore.utils.gpu_accelerator import GPUAccelerator
        
        def detect_gpu_background():
            try:
                gpu = GPUAccelerator()
                gpu_info = gpu.detect_gpu()
                if gpu_info:
                    logger.info(f"Pre-initialization: GPU detected: {gpu_info.get('name', 'Unknown')}")
                else:
                    logger.info("Pre-initialization: No GPU detected, will use CPU mode")
            except Exception as e:
                logger.warning(f"Pre-initialization: GPU detection error: {e}")
        
        # Start GPU detection in background
        gpu_thread = threading.Thread(target=detect_gpu_background)
        gpu_thread.daemon = True
        gpu_thread.start()
        
        return True
    
    except ImportError as e:
        logger.error(f"Missing dependency: {e}")
        return False
    except Exception as e:
        logger.error(f"Initialization error: {e}")
        return False

def main():
    """
    Main entry point for Smore: Bitcoin Wallet Brute-force Tool.
    Initializes and runs the GUI application.
    """
    try:
        # Initialize CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Pre-load dependencies
        logger.info("Pre-loading dependencies...")
        dependencies_loaded = load_dependencies()
        
        if not dependencies_loaded:
            logger.error("Failed to load dependencies")
            sys.exit(1)
        
        # Import app after dependency checks
        from smore.gui.app import BruteForceApp
        
        # Start the application
        app = BruteForceApp()
        
        # Transfer buffered logs to app
        for log_entry in buffer_handler.get_logs():
            app.after(0, lambda entry=log_entry: app.update_log(entry))
        
        # Run the application
        app.mainloop()
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)
        
        # If GUI failed to start, show error in console
        print(f"\nERROR: {str(e)}")
        print("Please check the log file for details.")
        sys.exit(1)

if __name__ == "__main__":
    main() 