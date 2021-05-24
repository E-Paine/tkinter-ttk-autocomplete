#!/bin/env python3
from tkinter import ttk
from typing import Iterable


class AutocompleteCombobox(ttk.Combobox):

    def __init__(self, master=None, autocomplete_words: Iterable[str] = (), **kw):
        super().__init__(master, **kw)
        self.set_autocomplete_words(autocomplete_words)
        self.bind("<KeyRelease>", self.__update_completions)

    def set_autocomplete_words(self, autocomplete_words: Iterable[str]):
        self.__autocomplete_words = sorted(list(autocomplete_words))
        self.__update_completions()

    def add_autocomplete_words(self, autocomplete_words: Iterable[str]):
        """
        Adds the given words to the completion list. This takes immediate effect.

        Time-complexity is O(n + k log(k))
        Space-complexity is O(n + k)

        :param autocomplete_words: iterable containing the words to be added
        :return: none
        """
        sorted_new_words = sorted(list(autocomplete_words))
        p1, p2 = 0, 0
        l1, l2 = len(self.__autocomplete_words), len(sorted_new_words)
        new_words = []
        while True:
            if p1 == l1:
                # we have already been through all of the old words list
                # therefore, we need to add the rest the new words list
                new_words.extend(sorted_new_words[p2:])
                break
            elif p2 == l2:
                # opposite of the previous branch
                new_words.extend(self.__autocomplete_words[p1:])
                break
            elif self.__autocomplete_words[p1] < sorted_new_words[p2]:
                # next word in our existing list is less, so we add that
                new_words.append(self.__autocomplete_words[p1])
                p1 += 1
            else:
                # next word in our existing list is less, so we add that
                new_words.append(sorted_new_words[p2])
                p2 += 1
        self.__autocomplete_words = new_words
        self.__update_completions()

    def __update_completions(self, event=None):
        pass
