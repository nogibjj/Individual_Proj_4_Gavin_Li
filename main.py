from flask import Flask, render_template, request
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


@app.route("/")
def index():
    nba_teams = [
        "Atlanta Hawks",
        "Boston Celtics",
        "Brooklyn Nets",
        "Charlotte Hornets",
        "Chicago Bulls",
        "Cleveland Cavaliers",
        "Dallas Mavericks",
        "Denver Nuggets",
        "Detroit Pistons",
        "Golden State Warriors",
        "Houston Rockets",
        "Indiana Pacers",
        "Los Angeles Clippers",
        "Los Angeles Lakers",
        "Memphis Grizzlies",
        "Miami Heat",
        "Milwaukee Bucks",
        "Minnesota Timberwolves",
        "New Orleans Pelicans",
        "New York Knicks",
        "Oklahoma City Thunder",
        "Orlando Magic",
        "Philadelphia 76ers",
        "Phoenix Suns",
        "Portland Trail Blazers",
        "Sacramento Kings",
        "San Antonio Spurs",
        "Toronto Raptors",
        "Utah Jazz",
        "Washington Wizards",
    ]
    return render_template("index.html", teams=nba_teams)


@app.route("/team")
def team():
    selected = request.args.get("selectedOption")
    ## TODO call OpenAI API, get a introduction
    prompt = f"give me a short introduction for {selected}"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    rslt = response.choices[0].message["content"]
    return render_template("result.html", selected=selected, intro=rslt)


def a():
    assert 1 == 1


if __name__ == "__main__":
    app.run(port=8000)
