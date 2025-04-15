#!/usr/bin/env python3
"""
Smore - Bitcoin Wallet Brute-force Tool (Optimized Launcher)
This script lets you choose between different GUI backends for optimal performance.
"""

import os
import sys
import time
import logging
import argparse
import multiprocessing
import importlib.util
from pathlib import Path

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("__main__")

def check_module_available(module_name):
    """Check if a Python module is available (installed)"""
    return importlib.util.find_spec(module_name) is not None

def setup_environment():
    """Set up environment for the application"""
    # Add application directory to path
    app_dir = Path(__file__).resolve().parent
    if str(app_dir) not in sys.path:
        sys.path.insert(0, str(app_dir))
    
    # Create logs directory if it doesn't exist
    logs_dir = app_dir / "smore" / "logs"
    logs_dir.mkdir(exist_ok=True)

def pre_load_dependencies():
    """Pre-load dependencies for faster startup"""
    logger.info("Pre-loading dependencies...")
    
    try:
        # Import core backend dependencies
        import numpy
        import hashlib
        import ecdsa
        import base58
        
        # Try to detect GPU and hardware features
        try:
            from smore.utils.gpu_accelerator import GPUAccelerator
            accelerator = GPUAccelerator()
            gpu_info = accelerator.detect_gpu()
            if gpu_info:
                logger.info(f"Pre-initialization: GPU detected: {gpu_info.get('name', 'Unknown GPU')}")
            else:
                logger.info("Pre-initialization: No GPU detected, using CPU mode")
        except Exception as e:
            logger.warning(f"Error during GPU detection: {e}")
            
    except ImportError as e:
        logger.warning(f"Missing dependency during pre-loading: {e}")
        logger.warning("Please run: pip install -r requirements.txt")

def main():
    """Main entry point for the optimized launcher"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Smore - Bitcoin Wallet Brute-force Tool")
    parser.add_argument("--gui", choices=["ctk", "qt", "auto"], default="auto",
                      help="GUI backend to use: 'ctk' for customtkinter, 'qt' for PyQt")
    parser.add_argument("--cores", type=int, default=0,
                      help="Number of CPU cores to use (0 for auto-detect)")
    parser.add_argument("--no-splash", action="store_true",
                      help="Skip splash screen")
    args = parser.parse_args()
    
    # Set up environment
    setup_environment()
    
    # Pre-load dependencies in the background
    preload_process = multiprocessing.Process(target=pre_load_dependencies)
    preload_process.start()
    
    # Determine GUI backend to use
    gui_backend = args.gui
    if gui_backend == "auto":
        # Auto-detect best available backend
        if check_module_available("PyQt5") or check_module_available("PyQt6"):
            gui_backend = "qt"
            logger.info("Auto-selected PyQt GUI backend for optimal performance")
        else:
            gui_backend = "ctk"
            logger.info("Auto-selected customtkinter GUI backend")
    
    # Show splash screen unless disabled
    if not args.no_splash:
        try:
            if gui_backend == "qt":
                # Qt splash screen
                if check_module_available("PyQt5"):
                    from PyQt5.QtWidgets import QApplication
                    from PyQt5.QtCore import Qt, QTimer
                    from PyQt5.QtGui import QPixmap
                    from PyQt5.QtWidgets import QSplashScreen
                else:
                    from PyQt6.QtWidgets import QApplication
                    from PyQt6.QtCore import Qt, QTimer
                    from PyQt6.QtGui import QPixmap
                    from PyQt6.QtWidgets import QSplashScreen
                
                app = QApplication(sys.argv)
                splash_img = QPixmap(str(Path(__file__).parent / "smore" / "assets" / "splash.png"))
                splash = QSplashScreen(splash_img, Qt.WindowStaysOnTopHint)
                splash.show()
                
                # Process events to show splash immediately
                app.processEvents()
                
                # Function to start the main app after delay
                def start_app():
                    splash.close()
                    if gui_backend == "qt":
                        from smore.gui_qt.app import start_qt_app
                        start_qt_app(args)
                    else:
                        from smore.gui.splash import show_splash_screen
                        from smore.gui.app import BruteForceApp
                        root = show_splash_screen()
                        app = BruteForceApp(root)
                        app.mainloop()
                
                # Wait for preloading to finish
                preload_process.join()
                
                # Start the app after a short delay
                QTimer.singleShot(1500, start_app)
                sys.exit(app.exec() if hasattr(app, 'exec') else app.exec_())
            else:
                # customtkinter splash screen
                from smore.gui.splash import show_splash_screen
                from smore.gui.app import BruteForceApp
                root = show_splash_screen()
                
                # Wait for preloading to finish
                preload_process.join()
                
                app = BruteForceApp(root)
                app.mainloop()
        except Exception as e:
            logger.error(f"Error during splash screen: {e}")
            # Fall back to direct start without splash
            args.no_splash = True
    
    # Direct start without splash
    if args.no_splash:
        # Wait for preloading to finish
        preload_process.join()
        
        if gui_backend == "qt":
            try:
                from smore.gui_qt.app import start_qt_app
                start_qt_app(args)
            except ImportError as e:
                logger.error(f"Failed to load PyQt interface: {e}")
                logger.info("Falling back to customtkinter interface")
                from smore.gui.app import BruteForceApp
                app = BruteForceApp()
                app.mainloop()
        else:
            from smore.gui.app import BruteForceApp
            app = BruteForceApp()
            app.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled exception: {e}", exc_info=True)
        sys.exit(1) 