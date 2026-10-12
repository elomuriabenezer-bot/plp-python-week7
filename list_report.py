# Week 7 Part C: List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Shopping items:")
for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")

long_name_count = 0
for item in items:
    if len(item) > 4:
        long_name_count += 1

longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print("Names with more than 4 letters:", long_name_count)
print("Longest item name:", longest_item)
