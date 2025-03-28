import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Initialize Flask app
app = Flask(__name__)

# Fetch historical stock data for training
def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)
    return hist['Close'].values if not hist.empty else None

# Train a simple ML model to predict future portfolio value
def train_portfolio_model(tickers):
    X, y = [], []
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')  # 1 year of data
    end_date = datetime.now().strftime('%Y-%m-%d')

    for ticker in tickers:
        prices = fetch_stock_data(ticker, start_date, end_date)
        if prices is not None and len(prices) > 10:  # Ensure enough data
            # Features: index (time), past price; Target: next price
            for i in range(len(prices) - 1):
                X.append([i, prices[i]])  # Time step and current price
                y.append(prices[i + 1])   # Next day's price

    if not X or not y:
        return None  # No valid data to train

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Predict future portfolio value
def predict_portfolio_value(model, tickers, shares, days_ahead=30):
    if not model:
        return 0
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    portfolio_value = 0
    for ticker, num_shares in shares.items():
        prices = fetch_stock_data(ticker, start_date, end_date)
        if prices is not None and len(prices) > 0:
            last_price = prices[-1]
            # Predict price in `days_ahead` days
            pred_price = model.predict([[len(prices), last_price]])[0]
            portfolio_value += pred_price * num_shares
    return portfolio_value

# Analyze finances and investments
def analyze_finances(data):
    total_expenses = sum(data["expenses"].values())
    surplus = data["income"] - total_expenses
    net_worth = data["savings"]

    # Current portfolio value
    tickers = list(data["investments"].keys())
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    stock_prices = {}
    for ticker in tickers:
        prices = fetch_stock_data(ticker, start_date, end_date)
        if prices is not None:
            stock_prices[ticker] = prices[-1]

    portfolio_value = 0
    for ticker, shares in data["investments"].items():
        if ticker in stock_prices:
            portfolio_value += shares * stock_prices[ticker]
    net_worth += portfolio_value

    # Train ML model and predict future value
    model = train_portfolio_model(tickers)
    future_portfolio_value = predict_portfolio_value(model, tickers, data["investments"]) if model else portfolio_value

    recommendations = []
    if surplus > 0:
        recommendations.append(f"Monthly surplus: ${surplus}. Consider saving ${surplus*0.6:.2f} and investing ${surplus*0.4:.2f}.")
    if data["savings"] < data["goals"]["emergency_fund"]:
        shortfall = data["goals"]["emergency_fund"] - data["savings"]
        recommendations.append(f"Emergency fund shortfall: ${shortfall:.2f}. Prioritize savings.")
    if portfolio_value > 0:
        recommendations.append(f"Current portfolio value: ${portfolio_value:.2f}. Predicted value in 30 days: ${future_portfolio_value:.2f}.")

    return {
        "total_expenses": total_expenses,
        "surplus": surplus,
        "net_worth": net_worth,
        "portfolio_value": portfolio_value,
        "future_portfolio_value": future_portfolio_value,
        "recommendations": recommendations
    }

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Parse form data
        income = float(request.form.get('income', 0))
        expenses = {
            "rent": float(request.form.get('rent', 0)),
            "groceries": float(request.form.get('groceries', 0)),
            "entertainment": float(request.form.get('entertainment', 0)),
            "utilities": float(request.form.get('utilities', 0))
        }
        savings = float(request.form.get('savings', 0))
        
        # Dynamic investments from user input
        investments = {}
        for key in request.form:
            if key.startswith('ticker_') and request.form[key]:
                ticker = request.form[key].upper()
                shares_key = f"shares_{key.split('_')[1]}"
                shares = float(request.form.get(shares_key, 0))
                if shares > 0:
                    investments[ticker] = shares

        goals = {
            "emergency_fund": float(request.form.get('emergency_fund', 0)),
            "retirement": float(request.form.get('retirement', 0))
        }

        # Analyze the data
        user_data = {
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "investments": investments,
            "goals": goals
        }
        result = analyze_finances(user_data)
        return render_template('index.html', result=result)

    # Default GET request: show form
    return render_template('index.html', result=None)

@app.route('/chat')
def chat():
    return '''
    <h2>Redirecting to Chatbot...</h2>
    <script>
        window.location.href = "http://localhost:8501"; // Redirect to Streamlit app
    </script>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)