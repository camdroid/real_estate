'''
Tools to make searching Zillow easier
'''

import argparse
from secrets import ZILLOW_WSID
import xml.etree.ElementTree as ET
import requests



def get_zillow_property_id(address, zip_code):
    ''' Get the ZPID from the address and zip code '''
    url = 'http://www.zillow.com/webservice/GetSearchResults.htm'
    params = {
        'zws-id': ZILLOW_WSID,
        'address': address,
        'citystatezip': zip_code,
    }
    res = requests.get(url, params)
    root = ET.fromstring(res.text)
    e_zpid = root.find('response/results/result/zpid')
    zpid = e_zpid.text
    return zpid


def get_property_details(zpid):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('address')
    parser.add_argument('zip')
    args = parser.parse_args()
    res = get_zillow_property_id(args.address, args.zip)
    print(res)

if __name__ == '__main__':
    main()
