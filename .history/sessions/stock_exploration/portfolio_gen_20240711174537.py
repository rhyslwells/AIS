import pandas as pd
import xlsxwriter

# Create a new Excel file and add sheets
file_path = '/mnt/data/Portfolio_Tracker.xlsx'
writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

# Create Dashboard DataFrame
dashboard_data = {
    "Stock": ["JPM", "GOOGL", "BABA", "AMZN", "AAPL", "COST", "MSFT", "CRM", "VUSA", "NFLX"],
    "Ticker": ["JPM", "GOOGL", "BABA", "AMZN", "AAPL", "COST", "MSFT", "CRM", "VUSA", "NFLX"],
    "Quantity": [0]*10,  # Placeholder for now
    "Avg. Purchase Price": [0.0]*10,  # Placeholder for now
    "Current Price": [0.0]*10,  # Placeholder for now
    "Market Value": [0.0]*10,  # Placeholder for now
    "Gain/Loss": [0.0]*10,  # Placeholder for now
    "Gain/Loss (%)": [0.0]*10  # Placeholder for now
}
df_dashboard = pd.DataFrame(dashboard_data)
df_dashboard.to_excel(writer, sheet_name='Dashboard', index=False)

# Create Watchlist DataFrame
watchlist_data = {
    "Stock": ["Visa", "BP"],
    "Ticker": ["V", "BP"],
    "Current Price": [0.0, 0.0],  # Placeholder for now
    "Target Price": [0.0, 0.0],  # Placeholder for now
    "Notes": ["", ""]
}
df_watchlist = pd.DataFrame(watchlist_data)
df_watchlist.to_excel(writer, sheet_name='Watchlist', index=False)

# Create Transaction History DataFrame
transaction_history_data = {
    "Date": [],
    "Stock": [],
    "Ticker": [],
    "Type (Buy/Sell)": [],
    "Quantity": [],
    "Price": [],
    "Total Value": []
}
df_transaction_history = pd.DataFrame(transaction_history_data)
df_transaction_history.to_excel(writer, sheet_name='Transaction History', index=False)

# Save the Excel file
writer.save()
file_path
