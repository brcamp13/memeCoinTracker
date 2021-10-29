import constants
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_meme_coins_from_api():
    # api_meme_coin_search_strings = constants.MEME_COIN_SEARCH_STRINGS
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
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
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    

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
    get_meme_coins_from_api()
    # Create a new file called potentialMemeCoin_s<DATE>_<TIME HH:MM:SS>
    # Check if meme coin folder exists locally, if not, create it, otherwise add new file to it
    # Print out the meme coin findings as well & inform user of file name that they've been saved to