import datetime

from flask import Flask, abort, render_template

FAVORITES = [
    {"id": 1, "title": "Any dark chocolate", "why": "Because oh my lanta so good"},
    {"id": 2, "title": "Kitkat", "why": "Because so crispy"},
    {"id": 3, "title": "Milkyway", "why": "Messes up my teeth but still adore"},
    {"id": 4, "title": "M&Ms", "why": "Melts in your mouth, not in your hand!!"}
]

COOL_DISTROS = [
    {"id": 1, "name": "Mint Cinnamon Edition", "experience": "first time using linux, it wouldn't boot for whatever reason and made me feel like a failure", "rating": 0},
    {"id": 2, "name": "Mint MATE Edition", "experience": "actually booted, worked great for dipping my toes into linux", "rating": 7},
    {"id": 3, "name": "Ubuntu Desktop", "experience": "felt clunky, I despised the task bar on the side and didn't know how to change it", "rating": 5},
    {"id": 4, "name": "Fedora Workstation (Gnome)", "experience": "fedora and Gnome are extremely intuitive, they go together like PB&J", "rating": 9},
    {"id": 5, "name": "Fedora KDE Plasma", "experience": "same inner workings as last entry but OMG WITH KDE YOU CAN CUSTOMIZE EVERYTHING", "rating": 10}
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

def index():
    return render_template(
        "index.html",
        name="Bernardo",
        hobby="poking around with linux",
        hours_per_week=3,  # roughly how many hours a week you spend on it
        fun_fact="I have no middle name",
        hour=datetime.time().hour,
        show_counter=False,
        favorites=FAVORITES
    )

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)

def linux_distros():
    return render_template(
        "distros.html",
        distros=COOL_DISTROS


    )

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/distros")(linux_distros)

def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
