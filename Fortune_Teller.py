import random
import time

choice_list = {
    "love": [
        "A long-lost connection will resurface when you least expect it.",
        "Someone close to you has feelings they haven't shared yet.",
        "A small act of kindness will lead to a surprising romantic turn.",
        "Be patient—love will arrive when you stop searching for it.",
        "A past mistake in love will teach you something valuable soon."
            ],
    "wealth": [
        "An unexpected opportunity will bring financial gain.",
        "A small risk today could lead to great rewards in the future.",
        "Be mindful of unnecessary spending—something valuable is coming your way.",
        "A past investment will soon pay off in ways you didn't anticipate.",
        "The key to financial success is closer than you think—pay attention to details."
        ],
    "misc": [
        "A random encounter will change your perspective on something important.",
        "Trust your instincts—they will guide you toward an important decision.",
        "A surprising piece of news will brighten your week.",
        "Someone you least expect will offer you valuable advice soon.",
        "Beware of distractions—your focus will determine your success."
            ]
}

# Pick a number from 1 - 4
print("Here is a list of categories to choose from: \n~ Love \n~ Career \n~ Misc")

pickCategory = str(input("Pick one category to receive your fortune: "))

while True:
    if pickCategory == "Love":
        print("Processing your fortune...")
        time.sleep(3)
        print("Here is your fortune: " + random.choice(choice_list["love"]))
    elif pickCategory == "Wealth":
        print("Processing your fortune...")
        time.sleep(3)
        print("Here is your fortune: " + random.choice(choice_list["wealth"]))
    elif pickCategory == "Misc":
        print("Processing your fortune...")
        time.sleep(3)
        print("Here is your fortune: " + random.choice(choice_list["misc"]))
    else:
        print("Invalid selection. No fortune for you.")

    time.sleep(3.5)
    play_again = input("Do you want to get another fortune? (Yes / No): ")
    if play_again != "Yes":
        print("Goodbye.")
        break