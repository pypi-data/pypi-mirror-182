import requests
import argparse
import xml.etree.ElementTree as ET

API_URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

def get_rates():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.text

def get_rate(currency: str) -> float:
    rates = get_rates()
    root = ET.fromstring(rates)
    for cube in root.findall('.//{*}Cube')[2:]:
        if cube.attrib['currency'] == currency:
            return float(cube.attrib['rate'])
    raise ValueError(f'Unknown currency {currency}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('currency', help='Currency to convert to')
    args = parser.parse_args()
    
    rate = get_rate(args.currency)
    print(f'1 EUR = {rate} {args.currency}')

if __name__ == '__main__':
    raise(SystemExit(main()))
