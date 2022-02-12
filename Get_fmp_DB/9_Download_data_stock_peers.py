# Download financial data from the Json List: Stock Peers
# Json list has all the tickers for a single exchange

# Imports
import os
import requests
import pandas as pd
import json
from sqlalchemy import create_engine

# Importing API Key
api = os.environ.get("token_finmodelprep")

# Stock Peers Variables
fin_data = "/stock_peers"
sqlite_table = "stock_peers"
www = "https://financialmodelingprep.com/api/v4"

# Open Json File with ticker list and save as variable
with open("ticker_list.json", "r") as f:
    ticker_list = json.load(f)

# Create Error file
f = open("error_list.txt", "a")
f.write("\n\nStock Peers Error List:\n")
f.close()

# Importing data from Financial Modeling Prep
for company in ticker_list:
    print("Company: " + company)
    try:
        # Creating Output Dataframe
        df_output = pd.DataFrame(columns=["symbol", "peers"])

        # Paste fmp_data link here:
        fmp_data = requests.get(f"{www}{fin_data}?symbol={company}&apikey={api}").json()

        # Save financial data as Dataframe
        df = pd.DataFrame(fmp_data)

        # Get the length of the peer list
        r = len(df["peersList"][0])

        # Append output dataframe with peers for each company
        for x in range(r):
            df_output.loc[len(df_output.index)] = [company, df["peersList"][0][x]]

        # Create an engine
        engine = create_engine("sqlite:///financialmodelingprep.db", echo=True)
        sqlite_connection = engine.connect()

        # Create a table
        df_output.to_sql(
            sqlite_table, sqlite_connection, if_exists="append", index=False
        )

        # Close connection
        sqlite_connection.close()

    except Exception:
        f = open("error_list.txt", "a")
        f.write("\n" + company)
        f.close()
        pass
