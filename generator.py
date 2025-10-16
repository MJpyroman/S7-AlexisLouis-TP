import random

def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def generate_name():
    words = load_words("words.txt")
    return f"{random.choice(words)} {random.choice(words)}"

if __name__ == "__main__":
    print("Bienvenue dans le Team Name Generator !")
    print("Voici ton nom d'équipe aléatoire :", generate_name())
