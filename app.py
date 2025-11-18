from flask import Flask
from market_reader_api.stocks.routes import stocks_bp

app = Flask(__name__)
app.register_blueprint(stocks_bp)


if __name__ == "__main__":
    app.run(debug=True)
