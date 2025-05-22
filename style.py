import random

# Picking a random storyteller style for kids
storyteller_styles = [
    "Tell the story in the voice of a cozy grandmother.",
    "Tell the story like a gentle forest spirit whispering.",
    "Tell the story with a sing-songy rhyme like a bard.",
    "Tell the story like a sleepy cloud floating by.",
]

def get_storyteller_intro():
    return random.choice(storyteller_styles)
