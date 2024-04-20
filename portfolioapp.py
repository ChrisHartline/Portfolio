import yfinance as yf
import pandas as pd

# Set the start and end dates for the historical data
start_date = "2018-01-01"
end_date = "2023-03-09"

# Download the historical data for MNST and CSCO
mnst_data = yf.download("MNST", start=start_date, end=end_date)
csco_data = yf.download("CSCO", start=start_date, end=end_date)

# Calculate the daily returns for both stocks
mnst_returns = mnst_data["Adj Close"].pct_change()
csco_returns = csco_data["Adj Close"].pct_change()

# Combine the returns into a single DataFrame
returns_data = pd.DataFrame({"MNST": mnst_returns, "CSCO": csco_returns})

# Calculate the correlation coefficient
correlation_coefficient = returns_data["MNST"].corr(returns_data["CSCO"])

print(f"The correlation coefficient between MNST and CSCO is: {correlation_coefficient:.2f}")