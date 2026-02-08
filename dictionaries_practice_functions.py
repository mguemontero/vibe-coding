
# Smoothie Bar: Count the Ingredients
# Customers keep ordering smoothies. Count how many times each ingredient appears.

def count_smoothie_ingredients(orders):
    counts = {}
    for ingredient in orders:
        counts[ingredient] = counts.get(ingredient, 0) + 1
    return counts

# Lost‑and‑Found Desk
# Look up who owns a lost item.

def find_owner(lost_items, item):
    return lost_items.get(item, "No owner listed")

# Café Menu Price Update
# Update the price of an item or add it if it doesn’t exist.

def update_price(menu, item, price):
    menu[item] = price
    return menu

# Pet Hotel: Group Pets by Species
# Given a list of pet names, group them by their first letter.

def group_pets(pets):
    groups = {}
    for pet in pets:
        letter = pet[0].lower()
        groups.setdefault(letter, []).append(pet)
    return groups

# Classroom Attendance Tracker
# Count how many times each student was marked present.

def attendance_count(records):
    counts = {}
    for name in records:
        counts[name] = counts.get(name, 0) + 1
    return counts

# Recipe Book: Get Ingredient Info
# Recipes are stored as nested dictionaries.

def get_ingredient(recipe, section, ingredient):
    return recipe.get(section, {}).get(ingredient, "Not found")

# Wardrobe Organizer
# Flatten a wardrobe where each drawer contains items.

def flatten_wardrobe(wardrobe):
    flat = {}
    for drawer, items in wardrobe.items():
        for item, qty in items.items():
            flat[item] = qty
    return flat

# Plant Watering Log
# Find which plants need water today (value = "today").

def plants_to_water(schedule):
    return [plant for plant, day in schedule.items() if day == "today"]

# Bakery Order Comparison
# Compare yesterday’s and today’s orders.

def compare_orders(old, new):
    added = {k: new[k] for k in new if k not in old}
    removed = {k: old[k] for k in old if k not in new}
    changed = {k: (old[k], new[k]) for k in old if k in new and old[k] != new[k]}
    return {"added": added, "removed": removed, "changed": changed}

# Mood Journal Word Index
# Index where each word appears in a journal entry.

def word_positions(text):
    index = {}
    words = text.split()
    for pos, word in enumerate(words):
        index.setdefault(word, []).append(pos)
    return index
