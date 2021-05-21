from flask import Flask, render_template, request, redirect, url_for
import Application.application as application
import json


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/login')
    def login():
        return render_template("login.html")

    @app.route('/register')
    def register():
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
            if request.form['submit_button'] == 'Show Top Gainers Today':
                data = application.get_top('gainers')
            elif request.form['submit_button'] == 'Show Top Losers today':
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

    return app


if __name__ == '__main__':
    create_app().run()
