# Week 7 Assignment: Shopping List Manager

- `list_warmup.py` practices list indexing, `append()`, `remove()`, and `len()`.
- `shopping_list.py` lets a user add, remove, and display shopping items in a menu loop.
- `list_report.py` numbers the given items, counts names longer than four characters, and finds the longest name.
- `screenshots/` is for screenshots showing each program running.

Checking whether an item is in the list before calling `.remove()` prevents a `ValueError` when the item is missing. It also lets the program show a helpful message and continue running. This makes removal predictable and safer for the user.
