from flask import Flask, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
import Application.application as application
import json
from Application.database import db_session, init_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite'
    )
    db = SQLAlchemy(app)
    init_db()

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = application.login(username, password)
            if not user:
                return redirect(url_for('login', error="Invalid username or password"))
            g.user = user
            return redirect(url_for('home'))
        return render_template("login.html")

    @app.route('/register', methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]
            rpassword = request.form["rpassword"]
            if password == rpassword:
                if application.register(username, email, password):
                    return redirect(url_for('login'))
                else:
                    return redirect(url_for('login', error="Username already exists"))
            else:
                return redirect(url_for('register', error="Passwords do not match"))
            return render_template("register.html")
        return render_template("register.html")

    @app.route('/graph')
    def graph():
        return render_template("graph.html")

    @app.route('/tops', methods=['GET', 'POST'])
    def tops():
        if request.method == 'GET':
            return render_template("tops.html")
        else:
            data = {}
            if request.form['submit_button'] == 'Show Top GAINERS Today':
                data = application.get_top('gainers')
            elif request.form['submit_button'] == 'Show Top LOSERS today':
                data = application.get_top('losers')
            return redirect(url_for('table', data=data))

    @app.route('/table')
    def table():
        return render_template("table.html", data=json.loads(request.args.get('data')))

    @app.route('/get_graph_api')
    def get_graph_api():
        stock = request.args.get('stock', None)
        start_date = request.args.get("start_date", None)
        return application.get_graph_with_indicators(stock, start_date)

    @app.route('/get_stats_api')
    def get_stats():
        stock = request.args.get('stock', None)
        return application.get_stats(stock)

    db.create_all()
    return app


if __name__ == '__main__':
    create_app().run()
