from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GAMES = {
    "fruits": {
        "grid": [
            list("APPLERQTY"),
            list("BNANAZXCV"),
            list("ORANGEMP"),
            list("GRAPEFJK"),
            list("MANGOLIU"),
            list("CHERRYOP"),
            list("KIWIBERR"),
            list("PEACHXYZ")
        ],
        "words": ["APPLE", "BANANA", "ORANGE", "GRAPE", "MANGO", "CHERRY"]
    },
    "colors": {
        "grid": [
            list("REDBLUE"),
            list("GREENYL"),
            list("ORANGEP"),
            list("PURPLEX"),
            list("BLACKWT"),
            list("WHITEBK")
        ],
        "words": ["RED", "BLUE", "GREEN", "ORANGE", "PURPLE", "BLACK"]
    },
    "professions": {
        "grid": [
            list("DOCTORPL"),
            list("ENGINEER"),
            list("TEACHERX"),
            list("LAWYEROP"),
            list("NURSEABC"),
            list("ARTISTYZ")
        ],
        "words": ["DOCTOR", "ENGINEER", "TEACHER", "LAWYER", "NURSE", "ARTIST"]
    },
    "vehicles": {
        "grid": [
            list("CARTRUCK"),
            list("BUSPLANE"),
            list("BICYCLEX"),
            list("SCOOTERY"),
            list("TRACTORA"),
            list("BOATSHIP")
        ],
        "words": ["CAR", "TRUCK", "BUS", "PLANE", "BICYCLE", "BOAT"]
    }
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game/<category>")
def game(category):
    game = GAMES.get(category)
    if not game:
        return "Game not found", 404
    return render_template(
        f"{category}.html",
        grid=game["grid"],
        words=game["words"],
        category=category.capitalize()
    )

@app.route("/check/<category>", methods=["POST"])
def check_word(category):
    word = request.json.get("word", "").upper()
    return jsonify({"valid": word in GAMES[category]["words"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
