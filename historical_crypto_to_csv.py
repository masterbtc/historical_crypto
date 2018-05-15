# -*- coding: utf-8 -*-

"""
historical_crypto_to_csv.py
~~~~~~~~~~~~
:copyright: (c) 2018 by jyutzio
:license: MIT, see LICENSE for more details.
:repository: https://github.com/jyutzio/historical_crypto
"""

import argparse
import csv
from datetime import datetime, date
import re
import urllib.request

regex = '''
<td class="text-left">(.*?)</td>
<td .*="(.*)">.*</td>
<td .*="(.*)">.*</td>
<td .*="(.*)">.*</td>
<td .*="(.*)">.*</td>
<td .*="(.*)">.*</td>
<td .*="(.*)">.*</td>
'''

def format_date(date):
    ''' Formats the date given by CMC to iso 8601 date format.
    :param date: cmc formatted date string ex: "1 January, 2018"
    :return: iso 8601 date string ex: "2018-01-01"
    '''
    return datetime.strptime(date, '%b %d, %Y').strftime("%Y-%m-%d")


def main():
    parser = argparse.ArgumentParser(description='''
    Historical data from Coinmarketcap.com downloaded to csv format.
    ''')

    today = date.today().isoformat()
    parser.add_argument('coin',
                        type=str,
                        help='The crypto currency to download data for.')
    parser.add_argument('--start',
                        type=str,
                        help='Start date (default: 2013-04-28)',
                        default="2013-04-28",
                        metavar='YYYY-MM-DD')
    parser.add_argument('--end',
                        type=str,
                        help=f'End date (default: {today})',
                        default=today,
                        metavar='YYYY-MM-DD')

    args = parser.parse_args()
    try:
        start_date = datetime.strptime(args.start, '%Y-%m-%d').strftime("%Y%m%d")
        end_date = datetime.strptime(args.end, '%Y-%m-%d').strftime("%Y%m%d")

        url = (f"https://coinmarketcap.com/currencies/{args.coin}" +
            f"/historical-data/?start={start_date}&end={end_date}")
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
    except ValueError:
        raise ValueError("Incorrect data format: should be YYYY-MM-DD")
    except urllib.error.HTTPError:
        raise ValueError(f"Incorrect token format: {args.coin} not found")

    reg = re.compile(regex)
    data = reg.findall(html)

    data_start = format_date(data[-1][0])
    data_end = format_date(data[0][0])
    csvFile = open(f"{data_start}_{data_end}_{args.coin}.csv", 'w', newline='')
    csvWriter = csv.writer(csvFile, )

    header = ('date', 'open', 'high', 'low', 'close', 'volume', 'market_cap')
    csvWriter.writerow(header)

    for row in data:
        row_date = format_date(row[0])
        row_ = (row_date, row[1], row[2], row[3], row[4], row[5], row[6])
        csvWriter.writerow(row_)


if __name__ == "__main__":
    main()
