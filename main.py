from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    nba_teams = [
        "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", 
        "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", 
        "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers", 
        "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", 
        "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks", 
        "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", 
        "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", 
        "Utah Jazz", "Washington Wizards"
    ]
    return render_template("index.html", teams = nba_teams)

@app.route("/team")
def team():
    selected = request.args.get("selectedOption")
    ## TODO call OpenAI API, get a introduction
    return render_template(
        "result.html",
        selected=selected,
        intro=""
    )


if __name__ == "__main__":
    app.run()
