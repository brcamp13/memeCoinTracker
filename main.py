import constants
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_all_cryptocurrencies_from_api():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'convert':'USD',
        'sort_dir':'desc',
        'limit':'5000',
        'cryptocurrency_type':'tokens'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': constants.API_KEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        cryptocurrencies = data['data']
        cryptocurrency_names = [cryptocurrency['name'] for cryptocurrency in cryptocurrencies]
        return cryptocurrency_names
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return e

def get_meme_coins():
    all_cryptocurrencies = get_all_cryptocurrencies_from_api()
    meme_coins = []
    for meme_coin_search_string in constants.MEME_COIN_SEARCH_STRINGS:
        for cryptocurrency in all_cryptocurrencies:
            if meme_coin_search_string.upper() in cryptocurrency.upper():
                meme_coins.append(cryptocurrency)
    return set(meme_coins)
    

def create_meme_coins_file(meme_coins):
    return 'file created'

def check_if_meme_coins_folder_exists():
    return False

def create_meme_coins_folder():
    return True

def add_meme_coins_file_to_folder(meme_coins_file):
    return True

if __name__ == "__main__":
    # Query api w/ list of meme coin strings
    meme_coins = get_meme_coins()
    print(meme_coins)
    print(str(len(meme_coins)) + ' coins returned')
    # Create a new file called potentialMemeCoin_s<DATE>_<TIME HH:MM:SS>
    # Check if meme coin folder exists locally, if not, create it, otherwise add new file to it
    # Print out the meme coin findings as well & inform user of file name that they've been saved to