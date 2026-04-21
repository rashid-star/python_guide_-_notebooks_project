import random

subjects = [
    "MS Dhoni",
    "Virat Kohli",
    "Rahul Gandhi",
    "Rohit Sharma",
    "Sachin Tendulkar",
    "Narendra Modi",
    "Shah Rukh Khan",
    "Amitabh Bachchan",
    "Priyanka Chopra",
    "A group of Monkeys",
    "A group of Dogs",
    "Taxi drivers",
    "Mohammad Rashid"
]

actions = [
    "eats",
    "kicks",
    "launches",
    "orders",
    "buys",
    "sells",
    "throws",
    "dances with",
    "sings with",
    "runs away from",
    "celebrates with",
    "fights with",
    "hugs",
]

places_or_things = [
    "at the park",
    "at Red Fort",
    "in the market",
    "in the stadium",
    "in the mall",
    "during IPL match",
    "during a cricket match",
    "during a football match",
    "during a concert",
    "during a wedding",
    "during a party",
    "in Mumbai local train",
    "in Delhi metro",
    "with a plate of samosas",
    "with a plate of biryani",
]

funny_endings = [
    "crowd asks for replay",
    "internet goes crazy",
    "fans call it legendary",
    "nobody understands what happened",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    ending = random.choice(funny_endings)

    if random.choice([True, False]):
        headline = f"Breaking News: {subject} {action} {place_or_thing}."
    else:
        headline = f"Breaking News: {subject} {action} {place_or_thing} - {ending}."

    print(f"\n{headline}")

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input in {"no", "n"}:
        break
    if user_input not in {"yes", "y"}:
        print("Please type yes or no.")

print("\nThank you for using the Fake Headline Generator!")