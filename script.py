from binance_historical_data import BinanceDataDumper
import csv

data_dumper = BinanceDataDumper(
    path_dir_where_to_dump="./dump",
    asset_class="spot",  # spot, um, cm
    data_type="aggTrades",  # aggTrades, klines, trades
    data_frequency="1d",
)

# According to docs / class definition, data_dumper.get_list_all_trading_pairs() does not take any arguments
# can't get a specific ticker, but reasonably easy to return all tickers.
usdt_pairs = [pair for pair in data_dumper.get_list_all_trading_pairs() if pair.endswith("USDT")] # returns strings

with open('data/binance_listings.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['ticker', 'listed_on'])
    writer.writeheader()
    
    for pair in usdt_pairs:
        listing = {
            "ticker": pair,
            "listed_on": data_dumper.get_min_start_date_for_ticker(ticker=pair)
        }
        writer.writerow(listing)
