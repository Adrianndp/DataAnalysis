from flask import Flask, render_template, request, jsonify, abort, make_response
import Application.application as application

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
        return application.get_graph_with_ema("AAPL", "2020-01-01", "2021.01.01")
    else:
        return render_template("graph.html")


@app.route('/news')
def news():
    return render_template("news.html")


@app.route('/get_graph_api')
def get_graph_api():
    stock = request.args.get('stock', None)
    if not stock:
        return abort(404, "Not stock was given")
    if request.args.get("start_date"):
        return jsonify(application.get_graph_with_ema(stock, request.args.get("start_date")))
    return application.get_graph_with_ema(stock)
    # return jsonify({"name": "a"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
