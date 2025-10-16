from flask import Flask, render_template
import random

app = Flask(__name__)

def load_words():
    with open("words.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

@app.route("/")
def home():
    words = load_words()
    team_name = f"{random.choice(words)} {random.choice(words)}"
    return render_template("index.html", team_name=team_name)

if __name__ == "__main__":
    app.run()
