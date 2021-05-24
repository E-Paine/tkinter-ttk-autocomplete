import autocomplete
import tkinter as tk

root = tk.Tk()
accb = autocomplete.AutocompleteCombobox(
    root,
    ["abc", "abcd", "abd", "def", "ghi", "jkl"]
)
accb.add_autocomplete_words(["jkm", "ghj", "efg"])
accb.pack()
root.mainloop()
