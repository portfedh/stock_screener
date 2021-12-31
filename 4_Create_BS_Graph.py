# Create Balance Sheet Graph

# Imports
import pandas as pd
import plotly.graph_objects as go

# Import SQLite3 table
sqlite_table = "balance_sheet"
table = pd.read_sql(sqlite_table, "sqlite:///financialmodelingprep.db")
print(len(table))
table.head()

# Create a list to loop over
# Get the unique values
symbol_table = table.symbol.unique()
# Create a list from unique values
symbol_list = symbol_table.tolist()

# Create a new  Dataframe for the Graphs: graph_df
graph_df = table.copy(deep=True)

# Add percentage columns
graph_df["tot_liability_perc"] = round(((graph_df["totalLiabilities"] / graph_df["totalAssets"]) * 100), 0)
graph_df["tot_intang_equity_perc"] = round(((graph_df["goodwillAndIntangibleAssets"] / graph_df["totalAssets"]) * 100), 0)
graph_df["tot_equity_perc"] = round(((graph_df["totalStockholdersEquity"] / graph_df["totalAssets"]) * 100), 0)

# Sort the data years in ascending order
graph_df.sort_index(ascending=False, inplace=True)

# For loop to check list
years = 5
for ticker in symbol_list:
    # Get the company ticker
    company_name = ticker
    # Create new dataframe: Filter for the company ticker
    graph_df_x = graph_df[graph_df["symbol"] == ticker]
    # Get the defined amount of years
    graph_df_x = graph_df_x.iloc[-years:]
    # Get the currency of the company
    currency = graph_df_x.iloc[0]["reportedCurrency"]
    # Graph th Balance Sheet
    fig = go.Figure(
        data=[
            go.Bar(
                    name="Assets",
                    x=graph_df_x["calendarYear"],
                    y=graph_df_x["totalAssets"],
                    marker_color="#003B73",
                    offsetgroup=0,
                    ),
            go.Bar(
                    name="Equity",
                    x=graph_df_x["calendarYear"],
                    y=graph_df_x["totalStockholdersEquity"],
                    marker_color="#01949a",
                    offsetgroup=1,
                    ),
            go.Bar(
                    name="Liabilities",
                    x=graph_df_x["calendarYear"],
                    y=graph_df_x["totalLiabilities"],
                    marker_color="#db1f48",
                    offsetgroup=1,
                    base=graph_df_x["totalStockholdersEquity"],
                    ),
            go.Bar(
                    name="GW & Intangibles",
                    x=graph_df_x["calendarYear"],
                    y=graph_df_x["goodwillAndIntangibleAssets"],
                    marker_color="#746C70",
                    offsetgroup=2,
                    ),
             ]
    )

    fig.update_layout(
                      barmode="group",  # group or stack
                      title=str("Balance Sheet for: " + company_name),
                      xaxis_title="Year",
                      yaxis_title=("Amount $ " + currency),
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  xanchor="right",
                                  x=1, y=1.0),
                      width=800,
                      height=400,
    )
    fig.update_traces(texttemplate="%{y:.2s}",textposition="inside")
    file_name = "output/" + company_name + "_BS.png"
    fig.write_image(file_name, scale=2)
