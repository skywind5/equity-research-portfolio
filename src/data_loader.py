import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return {
        "financials": stock.financials,
        "balance_sheet": stock.balance_sheet,
        "cashflow": stock.cashflow,
        "info": stock.info
    }