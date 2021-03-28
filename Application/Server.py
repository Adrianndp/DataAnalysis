from flask import Flask, render_template, request, abort
import Application.application as application

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/graph')
def graph():
    return render_template("graph.html")


@app.route('/statistics')
def statistics():
    return render_template("statistics.html")


@app.route('/tops', methods=['GET', 'POST'])
def tops():
    if request.method == 'POST':
        return application.df_to_csv("AAPL", "2020-01-01", "2021-01-01")
    else:
        return render_template("tops.html")


@app.route('/get_graph_api')
def get_graph_api():
    stock = request.args.get('stock', None)
    start_date = request.args.get("start_date", None)
    return application.get_graph_with_indicators(stock, start_date)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="localhost")
