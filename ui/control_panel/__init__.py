from .buttons import *
import tkinter as tk


class ControlPanel(tk.Frame):
    """A box that contains control buttons that play/pause, reset, does one swap, and show/hide districts"""

    def __init__(self, root):
        self.root = root
        super().__init__(root.ui_frame, bd=1, relief='solid')

        self.play_pause_button = PlayPauseButton(self)
        self.reset_button = ResetButton(self)
        self.swap_button = SwapButton(self)
        self.toggle_districts_button = ToggleDistrictsButton(self)

        self.play_pause_button.pack(side='left')
        self.reset_button.pack(side='left')
        self.swap_button.pack(side='left')
        self.toggle_districts_button.pack(side='left')
