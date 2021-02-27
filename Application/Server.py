from flask import Flask, render_template, request, abort
import Application.application as application

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/graph')
def graph():
    return render_template("graph.html")


@app.route('/news')
def news():
    return render_template("news.html")


@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        return application.df_to_csv("AAPL", "2020-01-01", "2021-01-01")
    else:
        return render_template("download.html")


@app.route('/get_<api>_api')
def get_graph_api(api):
    stock = request.args.get('stock', None)
    start_date = request.args.get("start_date", None)
    keyword = request.args.get("keyword", None)
    if api == "news":
        return application.get_news(keyword, start_date)
    elif api == "graph":
        return application.get_graph_with_ema(stock, start_date)
    else:
        return abort(500, "Bad request")


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="localhost")
