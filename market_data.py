import yfinance as yf

def fetch_market_data():
    tickers = {
        "S&P500": "^GSPC",
        "Nasdaq": "^IXIC",
        "VIX": "^VIX",
        "BTC": "BTC-USD"
    }

    result = {}

    for k, v in tickers.items():
        try:
            data = yf.Ticker(v).history(period="2d")
            result[k] = float(data["Close"].iloc[-1])
        except:
            result[k] = None

    return result
