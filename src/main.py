"""
Main entry point for the Algorithm Calculator application.
"""

import tkinter as tk
from ui import AlgorithmCalculator

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmCalculator(root)
    root.mainloop()