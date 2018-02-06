from urllib.request import urlopen
from urllib.parse import urlencode
import json
import os

def get_redirect_link():
    """ Build and return the OAuth login link

        return login URI
    """
    uri = os.environ.get('ETUUTT_BASE_URI') \
        + 'oauth/authorize?client_id=' \
        + os.environ.get('ETUUTT_CLIENT_ID') \
        + '&scope=public%20private_user_account&response_type=code&state=xyz'
    return uri

def get_access_code(authorization_code):
    """ Send the authorization_code to EtuUTT to get an access token

        Args:
            authorization_code -- string

        return strings: access_token, refresh_token
    """
    # prepare request
    body = {
        'client_id': os.environ.get('ETUUTT_CLIENT_ID'),
        'client_secret': os.environ.get('ETUUTT_CLIENT_SECRET'),
        'authorization_code': authorization_code,
        'grant_type': 'authorization_code'
    }
    encoded_body = bytes(urlencode(body).encode())
    uri = os.environ.get('ETUUTT_BASE_URI') + 'oauth/token'
    # make request
    res = urlopen(uri, encoded_body)
    # parse response
    res_body = json.loads(res.read().decode(res.info().get_param('charset') or 'utf-8'))
    # return access token and refresh token
    return res_body['access_token'], res_body['refresh_token']
