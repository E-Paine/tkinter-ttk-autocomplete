#!/bin/env python3
from tkinter import ttk


class AutocompleteCombobox(ttk.Combobox):

    def __init__(self, master=None, autocomplete_words=(), **kw):
        super().__init__(master, **kw)
        self.set_autocomplete_words(autocomplete_words)

    def set_autocomplete_words(self, autocomplete_words):
        pass

    def add_autocomplete_words(self, autocomplete_words):
        pass
