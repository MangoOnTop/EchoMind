"""EchoMind Modern Desktop GUI Launcher"""
import os
import sys

# Ensure root directory is on the python path
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.gui import run_gui

if __name__ == "__main__":
    run_gui()
