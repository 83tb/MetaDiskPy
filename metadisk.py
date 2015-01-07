import requests, json

metadisk_url = "http://node1.metadisk.org/"

# public
upload_url = metadisk_url + "api/upload"
download_url = metadisk_url + "api/download/"
find_url = metadisk_url + "api/find/"
status_url = metadisk_url + "api/status"
prices_url = metadisk_url + "/accounts/token/prices"
balance_url = metadisk_url + "/accounts/token/balance/"
token_url = metadisk_url + "/accounts/token/new"
redeem_url = metadisk_url + "/accounts/token/redeem/"


# private
deposit_url = metadisk_url + "/accounts/token/deposit/"
witdraw_url = metadisk_url + "/accounts/token/withdraw/"


#r = requests.post(metadisk_url, data, auth=('user', '*****'))


import simplejson

def upload(file):
    """
    POST /api/upload
    Parameters:
    - file

    """

    files = {'file': open(file, 'rb')}
    r = requests.post(upload_url, files=files)
    headers = r.headers
    filehash = r.json()['filehash']
    key = r.json()['key']
    return dict(filehash=filehash,key=key)

def download(filehash):
    """
    GET /api/download/<filehash>
    Parameters:
    - filehash

    """
    r = requests.get(download_url+filehash)
    return r.content


def find(filehash):
    """
    GET /api/find/<filehash>
    Parameters:
    - filehash

    """
    r = requests.get(find_url+filehash)
    return r.json()

def status():
    """
    GET /api/status
    Parameters: None

    """
    r = requests.get(status_url)
    return r.json()


def new_token():
    """
    POST /accounts/token/new
    Parameters: None
    """

    r = requests.post(token_url)

    token = r.json()['token']

    return dict(token=token)

def get_prices():
    """
    GET /accounts/token/prices
    Parameters: None

    """
    r = requests.get(prices_url)
    return r.json()


def get_balance(token):
    """
    GET /accounts/token/balance/<access_token>
    Parameters: None

    """
    r = requests.get(balance_url + token)
    return r.json()

def redeem_code(token, code):
    """
    POST /accounts/token/redeem/<access_token>
    Parameters:
    - promocode

    """
    r = requests.post(redeem_url+token, params={'promocode':code})
    return r.json()





def deposit(token, bytes1, secret):
    """
    POST /accounts/token/deposit/<access_token>
    Parameters:
    - bytes

    """
    r = requests.post(deposit_url+token, params={'bytes':bytes1}, auth=(secret))
    return r.json()

def witdraw(token, bytes1, secret):
    """
    POST /accounts/token/withdraw/<access_token>
    Parameters:
    - bytes
    
    """
    r = requests.post(witdraw_url+token, params={'bytes':bytes1}, auth=(secret))
    return r.json()


# Tests

#print download("bc2371a5592df676f0221bb940790cc389470e12c040e7fa79e1fedd4028f0e1?key=293902e516bce87b276d9f416d27059c6e9ce630ab15c38767ca63f5e2563cb9&token=XeWAT4uiQcBMqt2m")
#print upload("test.txt")
#print find("bc2371a5592df676f0221bb940790cc389470e12c040e7fa79e1fedd4028f0e1?key=293902e516bce87b276d9f416d27059c6e9ce630ab15c38767ca63f5e2563cb9&token=XeWAT4uiQcBMqt2m")
#print status()
#print new_token()
#print get_prices()
#print get_balance(new_token()['token'])
#print redeem_code(new_token()['token'],"432234")
