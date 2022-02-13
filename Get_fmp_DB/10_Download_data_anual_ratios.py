# Download financial data from the Json List: Anual Ratios
# Json list has all the tickers for a single exchange

# Imports
import os
import requests
import pandas as pd
import json
from sqlalchemy import create_engine

# Importing API Key
api = os.environ.get("token_finmodelprep")

# Annual Ratios (not TTM) Variables
fin_data = "/ratios/"
sqlite_table = "ratios"
www = "https://financialmodelingprep.com/api/v3"

# Open Json File and save as variable
with open("ticker_list.json", "r") as f:
    ticker_list = json.load(f)

# Create Error file
f = open("error_list.txt", "a")
f.write("\n\nAnnual Ratios Error List:\n")
f.close()

# Importing data from Financial Modeling Prep
for company in ticker_list:
    print(company)
    try:
        # Paste fmp_data link here:
        fmp_data = requests.get(
            f"{www}{fin_data}{company}?apikey={api}"
        ).json()

        # Save financial data as Dataframe
        df = pd.DataFrame(fmp_data)

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
        f.write("\n" + company)
        f.close()
        pass
