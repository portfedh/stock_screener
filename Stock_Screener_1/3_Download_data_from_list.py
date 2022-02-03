# Download financial data from the Json List.
# Json list has all the tickers for a single exchange

# Imports
import os
import requests
import pandas as pd
import json
from sqlalchemy import create_engine

# Importing API Key
api = os.environ.get("token_finmodelprep2")

# API Variables.
# Uncomment one group at a time and run the list.


# Income Statement
##################
# fin_data = "/income-statement/"
# sqlite_table = "income_statement"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Balance Sheet
###############
# fin_data = '/balance-sheet-statement/'
# sqlite_table = "balance_sheet"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Cash Flow Statement
#####################
# fin_data = '/cash-flow-statement/'
# sqlite_table = "cashflow_statement"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Profile
#########
# fin_data = '/profile/'
# sqlite_table = "profile"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Annual Key Metrics (not TTM)
##############################
# fin_data = '/key-metrics/'
# sqlite_table = "key_metrics"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Annual Ratios (not TTM)
#########################
# fin_data = '/ratios/'
# sqlite_table = "ratios"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Key Executives
################
# fin_data = '/key-executives/'
# sqlite_table = "key_executives"
# www = "https://financialmodelingprep.com/api/v3"
# fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

# Stock Peers
#############
# fin_data = '/stock_peers'
# sqlite_table = "stock_peers"
# www = "https://financialmodelingprep.com/api/v4"
# fmp_data = requests.get(f"{www}{fin_data}?symbol={company}&apikey={api}").json()


# Open Json File and save as variable
with open("ticker_list.json", "r") as f:
    ticker_list = json.load(f)

# Create Error file
f = open("error_list.txt", "w")
f.write("Error List:\n")
f.close()

# Importing data from Financial Modeling Prep
for company in ticker_list:
    print(company)
    try:
        # Paste fmp_data link here

        # Save financial data as Dataframe
        df = pd.DataFrame(fmp_data)

        # Transform column from string to date format
        df["date"] = pd.to_datetime(df["date"])
        df["fillingDate"] = pd.to_datetime(df["fillingDate"])
        df["acceptedDate"] = pd.to_datetime(df["acceptedDate"])

        # Create an engine
        engine = create_engine("sqlite:///financialmodelingprep.db", echo=True)
        sqlite_connection = engine.connect()

        # Create a table
        df.to_sql(sqlite_table,
                  sqlite_connection,
                  if_exists="append",
                  index=False)

        # Close connection
        sqlite_connection.close()
    except Exception:
        f = open("error_list.txt", "a")
        f.write("\n" + company + " Exception: " + Exception)
        f.close()
        pass
