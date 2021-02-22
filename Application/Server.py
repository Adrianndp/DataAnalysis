from flask import Flask, render_template, request, jsonify
import Application.application as application


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == 'POST':
        return application.get_close("AAPL", "2020-01-01", "2021.01.01")
    else:
        return render_template("graph.html")


@app.route('/news')
def news():
    return render_template("news.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
