"""
EchoMind Universal Launcher
Allows running either the modern Desktop GUI or the classic Terminal CLI.

Usage:
    python run.py         # Launches the modern Desktop GUI
    python run.py --cli   # Launches the Terminal CLI mode
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--cli", "-c", "cli", "terminal"]:
        from src.main import run_cli
        run_cli()
    else:
        from src.gui import run_gui
        run_gui()
