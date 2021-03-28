from flask import Flask, render_template, request, abort
import Application.application as application


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is None:
        app.config.from_pyfile('application.cfg', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/graph')
    def graph():
        return render_template("graph.html")

    @app.route('/statistics')
    def statistics():
        return render_template("statistics.html")

    @app.route('/tops')
    def tops():
        return render_template("tops.html")

    @app.route('/get_top_gainers')
    def get_top_gainers():
        return application.get_top_gainers()

    @app.route('/get_top_losers')
    def get_top_losers():
        return application.get_top_losers()

    @app.route('/get_top_active')
    def get_top_active():
        return application.get_top_active()

    @app.route('/get_graph_api')
    def get_graph_api():
        stock = request.args.get('stock', None)
        start_date = request.args.get("start_date", None)
        return application.get_graph_with_indicators(stock, start_date)

    @app.route('/get_stats_api')
    def get_stats():
        stock = request.args.get('stock', None)
        return application.get_stats(stock)

    app.debug = True
    app.host = "localhost"
    app.port = 500
    return app


if __name__ == '__main__':
    create_app().run(host="localhost")
