"""Module provides functionality for a labeled entry box."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk

from .common import funcs
from .common.constants import *


class LabeledEntry(tk.Frame):
    """Custom labeled entry contained by a frame.

    Class Extensions:
        Tkinter.Frame (python 2.X)
        tkinter.Frame (python 3.X)

    Tkinter Widget Codes:
        Frame: ['f']
        Label: ['l']
        Entry: ['e']
    """

    def __init__(self, parent, placeholder='', **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        frame_ops = funcs.extract_args(kwargs, FRAME_KEYS, FRAME_KEY)
        frame = tk.Frame(self, frame_ops)
        frame.pack(fill='both', expand=True)

        label_ops = funcs.extract_args(kwargs, LABEL_KEYS, LABEL_KEY)
        label = tk.Label(frame, label_ops)
        tvar = tk.StringVar()
        entry_ops = funcs.extract_args(kwargs, ENTRY_KEYS, ENTRY_KEY)
        entry_ops['textvariable'] = tvar
        self.entry = tk.Entry(frame, entry_ops)

        label.pack(side='top', fill='x', expand=True)
        self.entry.pack(side='bottom', fill='x', expand=True)
        # self.entry.focus_force()
        self.parent.columnconfigure(0, weight=1)
        self.insert = self.entry.insert
        self.delete = self.entry.delete
        self.get = self.entry.get
        self.set = tvar.set
        self.index = self.entry.index
        self.bind = self.entry.bind
        # self.state = lambda: change_state(self.entry)
        self.enable = lambda: funcs.set_state_normal(self.entry)
        self.normal = lambda: funcs.set_state_normal(self.entry)
        self.disable = lambda: funcs.set_state_disabled(self.entry)
        self.clear = lambda: funcs.clear(self.entry)

    def add_placeholder_to(self, placeholder, color="grey", font=None):
        funcs.add_placeholder_to(self.entry, placeholder, color, font)
