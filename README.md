# Stock Screener

## What it does

The script creates a PNG image showing a Company's Balance
Sheet for the last five fiscal years.

It's aim is to serve as a first level stock screener. 

The image will create a graph with the following information:
- Total Assets ($)
- Total Liabilities ($) 
- Total Equity ($)
- Total Goodwill and Ingangibles

An example of the output file can be seen in `6_Example_output.png`

The script is divided into several files that do the following:

1. Download the available stocks list from [FMP](https://financialmodelingprep.com/)
	- Download the available list of tickers from [FMP](https://financialmodelingprep.com/)
	- Filter out ETF's and Mutual Funds
	- Save filtered list to SQLite database

2. Create a list of stocks to evaluate by stock exchange
	- Read SQLite database
	- Filter database by stock exchange 
	- Save the list to a json file

3. Download the Balance Sheet information for the list
	- Open the json file
	- Create an error file
	- Use a for loop to go through the list and download the data
	- Save the Balance sheet data to an SQLite database
	- If there's an error, log the company name in the error file

4. Create Graphs for the selected companies
	- Read the SQLite database
	- Create a Graph for each company

- Filter the companies with the best Balance Sheets (Manually)

5. Create a List of the selected Balance Sheets for further analysis


### How to Install

To use this script, you must have previously installed:

- [Python 3](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/install)
- [Sqlalchemy](https://docs.sqlalchemy.org/en/14/intro.html#installation)
- [Requests](https://pypi.org/project/requests/)
- [Pandas](https://pypi.org/project/pandas/)
- [Plotly](https://pypi.org/project/plotly/)

You will also need a token from [Financial Modeling Prep](https://financialmodelingprep.com/) 
to be able to use the script. 

Financial Modeling prep is a stock data provider. 
They cover NYSE, NASDAQ, AMEX, EURONEX, TSX, INDEXES, ETFs, MUTUAL FUNDS, FOREX and CRYPTO. 

[Financial Modeling Prep](https://financialmodelingprep.com/) has a free version, which allows for 250 requests per day and covers all the US makets. 
Paid suscriptions give coverage to the rest of the stocks and an unlimited number of requests. 

## How to Use

### Setup:
1. Download the scripts.
1. Download the required dependencies.
1. In the same folder as the script add a folder named "output".

### Runing

1. Execute the first script.
2. Define the exchange to evaluate
3. Execute the second script. 
4. Execute the third script
5. Execute the fourth script
6. Evaluate the companies you are interested in.
7. Move the images to a folder you are interested
8. Execute the fifth script

The fifth script will search a folder in `path = ./output/1.Blue`. You can change its name to whatever works for you. 

You will end up with a list called `blue_list.json`. You can also change the name to whatever works for you.

Besides having a five year history of the balance sheets you are interested in, you can use this output list to further research the stocks.

There is another Repository named `Fundamental Analysis`, where a more extensive report of the company can be generated. 


## Use cases

The script is useful for anyone interested in exploring the financial position of several companies at a time. 


## Contributing

Some things that could make the script better could be:
- Automating the screening process to filter the best companies.
