# Create a CashFlow Statement

# Imports
import json
import pandas as pd
import plotly.graph_objects as go

# Read SQL Table
sqlite_table = "cashflow_statement"
table = pd.read_sql(sqlite_table, "sqlite:///financialmodelingprep.db")

# Import Blue list from second screener
blue_list = json.load(open('P&L_blue_list.json', 'r'))

# Create a new  Dataframe for the Graphs: graph_df
graph_df = table.copy(deep=True)

# Sort the data years in ascending order
graph_df.sort_index(ascending=False, inplace=True)

# For loop to check list
years = 10
for ticker in blue_list:
    # Get the company ticker
    company_name = ticker
    # Create new dataframe: Filter for the company ticker
    graph_df_x = graph_df[graph_df["symbol"] == ticker]
    # Get the defined amount of years
    graph_df_x = graph_df_x.iloc[-years:]
    # Get the currency of the company
    currency = graph_df_x.iloc[0]["reportedCurrency"]
    # Cash Flow Statement
    fig = go.Figure(data=[
            go.Bar(name='CF Operations',
                   x=graph_df_x["date"],
                   y=graph_df_x['netCashProvidedByOperatingActivities'],
                   marker_color='#01949A',
                   offsetgroup=2
                   ),
            go.Bar(name='CF Investing',
                   x=graph_df_x["date"],
                   y=graph_df_x['netCashUsedForInvestingActivites'],
                   marker_color='#004369',
                   offsetgroup=3,
                   ),
            go.Bar(name='CF Financing',
                   x=graph_df_x["date"],
                   y=graph_df_x['netCashUsedProvidedByFinancingActivities'],
                   marker_color='#DB1F48',
                   offsetgroup=4,
                   )
        ])
    fig.update_layout(barmode='group',  # group or stack
                      title=str('Cash Flow Statement for: '+company_name),
                      xaxis_title='Year',
                      yaxis_title=('Amount $mm '+currency),
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.0,
                                  xanchor="right",
                                  x=1),
                      width=800,height=400)
    fig.update_traces(texttemplate='%{y:.2s}', textposition='inside')
    file_name = "output/" + company_name + ".png"
    fig.write_image(file_name, scale=2)
