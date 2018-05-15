# historical_crypto_to_csv.py

A simple script that scrapes coinmarketcap.com for historical prices of any chosen crypto currency, using only the python standard library.

Currently the script only accepts the slug/identifier that coinmarketcap uses. To get the slug for various cryptos, you can take it from the coinmarketcap url for the desired crypto.\
Example:
```
https://coinmarketcap.com/currencies/SLUG/
https://coinmarketcap.com/currencies/ethereum/
https://coinmarketcap.com/currencies/bitcoin/
```

## Requirements

- Python 3.6.5

## Quick start

All available historical data for Bitcoin
```
git clone https://github.com/historical_crypto/repo.git
cd historical_crypto
historical_crypto_to_csv.py bitcoin
```

## Usage

Arguments
- coin
  - The crypto currency to download data for
  - ex. bitcoin
  - required
  - must be a slug/identifer used on cmc
- --start
  - ex. 2017-12-31
  - optional
  - default: 2013-04-28, oldest data available
- --end
  - ex. 2018-01-31
  - optional
  - default: todays current date

The date inputs may be ommitted to collect all possible data for a specific coin.
```
historical_crypto_to_csv.py <coin> --start <start_date> --end <end_date>
```

## Examples
Ethereum data for 1 month. (Jan 2018)

```
historical_crypto_to_csv.py ethereum --start 2018-01-01 --end 2018-01-31
```
Ripple data since start of the year.
```
historical_crypto_to_csv.py ripple --start 2018-01-01
```
Bitcoin data up to the start of 2016
```
historical_crypto_to_csv.py bitcoin --end 2016-01-01
```

## License