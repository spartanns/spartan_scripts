# pip install yfinance
import yfinance as yf

stk = input("Enter share symbol: ").upper()

data = yf.Ticker(stk).history(period="1d")

last_market_price = data["Close"].iloc[-1]

print(f"Last market price {stk}: ${round(last_market_price, 2)}")
