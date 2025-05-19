import random

# Character name components
nick_prefixes = ["Cold", "Mad", "Iron", "Silent", "Bloody", "Lucky", "Broken", "Tired", "Broken"]
nick_suffixes = ["Dog", "Raven", "Jackal", "Fox", "Bear", "Vulture", "Shadow"]

# Pre-Zone professions
professions = [
    "Factory Worker", "Mechanic", "Night Watchman", "Soldier", "Smuggler", "Scavenger", "Paramedic", "Grave Digger", "Bus Driver", "Ex-Soldier", "Sailor"
]

# Motivations
motivations = [
    "Money", "Running from the law", "Redemption", "Looking for someone",
    "Scientific curiosity", "Following a dream", "No better options"
]
# Character alignment
alignment_prefix = ["Chaotic", "Neutral", "Lawful"]
alignment_suffix = ["Good", "Neutral", "Evil"]

# Starting items
starting_items = [
    "Old Hunting knife", "Toolkit", "Pocket flashlight",
    "Family photo", "Tattered raincoat", "Pack of cigarettes",
    "Vodka flask", "Personal Notebook", "Old Zippo Lighter", ""
]

# Locations
origins = ["Ukraine", "Belarus", "Russia", "Poland", "Latvia", "Moldova", "Romania", "Czechia", "Slovakia", "Bulgaria", "Estonia", "Lithuania", "Croatia", "Kosovo", "Herzegovina", "Turkey", ""]

def generate_character():
    name = f"{random.choice(nick_prefixes)} {random.choice(nick_suffixes)}"
    age = random.randint(24, 50)
    origin = random.choice(origins)
    profession = random.choice(professions)
    alignment = f"{random.choice(alignment_prefix)} {random.choice(alignment_suffix)}"
    motivation = random.choice(motivations)
    items = random.sample(starting_items, k=3)

    print("\n🎒 STALKER Character (Pre-Zone)")
    print("-------------------------------")
    print(f"Name (Nickname): {name}")
    print(f"Age: {age}")
    print(f"Origin: {origin}")
    print(f"Former Profession: {profession}")
    print(f"Alignment: {alignment}")
    print(f"Motivation to Enter the Zone: {motivation}")
    print("Starting Gear:")
    for item in items:
        print(f"  - {item}")
    print("-------------------------------\n")

# Run it
if __name__ == "__main__":
    generate_character()
