# Download financial data from List

# Imports
import os
import requests
import pandas as pd
import json
from sqlalchemy import create_engine

# Importing API Key
api = os.environ.get("token_finmodelprep2")

# Variables
# fin_data = "/income-statement/"
# sqlite_table = "income_statement"
fin_data = '/balance-sheet-statement/'
sqlite_table = "balance_sheet"
# fin_data = '/cash-flow-statement/'
# sqlite_table = "cashflow_statement"

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
        # Request financial data
        www = "https://financialmodelingprep.com/api/v3"
        fmp_data = requests.get(f"{www}{fin_data}{company}?apikey={api}").json()

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
        df.to_sql(sqlite_table, sqlite_connection, if_exists="append", index=False)

        # Close connection
        sqlite_connection.close()
    except:
        f = open("error_list.txt", "a")
        f.write("\n" + company)
        f.close()
        pass
