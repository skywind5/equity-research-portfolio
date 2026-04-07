import pandas as pd

def calculate_growth(series):
    return series.pct_change()

def calculate_margin(revenue, profit):
    return profit / revenue

def prepare_financials(financials_df):
    revenue = financials_df.loc["Total Revenue"]
    net_income = financials_df.loc["Net Income"]

    df = pd.DataFrame({
        "Revenue": revenue,
        "Net Income": net_income
    }).T.T

    df["Revenue Growth"] = calculate_growth(df["Revenue"])
    df["Net Margin"] = calculate_margin(df["Revenue"], df["Net Income"])

    return df