import constants
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import os


def get_all_cryptocurrencies_from_api():
    url = 'https://rest.coinapi.io/v1/assets'
    headers = {'X-CoinAPI-Key' : constants.COIN_IO_API_KEY}
    try:
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        cryptocurrency_names = [cryptocurrency['name'] for cryptocurrency in data]
        return cryptocurrency_names
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def get_meme_coins():
    all_cryptocurrencies = get_all_cryptocurrencies_from_api()
    meme_coins = []
    for meme_coin_search_string in constants.MEME_COIN_SEARCH_STRINGS:
        for cryptocurrency in all_cryptocurrencies:
            if meme_coin_search_string.upper() in cryptocurrency.upper():
                meme_coins.append(cryptocurrency)
    return sorted(set(meme_coins))
    

def create_meme_coins_file(meme_coins):
    datetime_file_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file_name = os.getcwd().join('meme_coins ' + datetime_file_string)

    os.chdir("memeCoins")

    with open(file_name, 'w') as f:
        for meme_coin in sorted(meme_coins):
            f.write("%s\n" % meme_coin)

    os.chdir('../')

    return file_name

def check_if_meme_coins_folder_exists():
    cwd = os.getcwd()
    return os.path.isdir(cwd + '/memeCoins')

def create_meme_coins_folder():
    os.mkdir("memeCoins")

def add_meme_coins_file_to_folder(meme_coins_file):
    return True

if __name__ == "__main__":
    # Check if meme coin folder exists locally, if not, create it
    if not check_if_meme_coins_folder_exists():
        create_meme_coins_folder()
    # Query api w/ list of meme coin strings
    meme_coins = get_meme_coins()
    # Create a new file called potentialMemeCoin_s<DATE>_<TIME HH:MM:SS>
    meme_coins_file_name = create_meme_coins_file(meme_coins)
    # Print out the meme coin findings as well & inform user of file name that they've been saved to
    print(meme_coins)
    print(str(len(meme_coins)) + ' coins returned')
    print('File with coins can be found in ' + os.getcwd() + '/' + meme_coins_file_name)
