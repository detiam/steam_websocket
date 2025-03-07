import requests
from binascii import hexlify
from steam.core.crypto import sha1_hash, random_bytes
from enum import Enum

class APIHost(Enum):
    """Enum of currently available API hosts."""
    Public = 'api.steampowered.com'
    """ available over HTTP (port 80) and HTTPS (port 443)"""
    China = 'api.steamchina.com'
    Partner = 'partner.steam-api.com'
    """available over HTTPS (port 443) only

    .. note::
        Key is required for every request. If not supplied you will get HTTP 403.
    """

DEFAULT_PARAMS = {
    # api parameters
    'apihost': APIHost.Public.value,
    'key': None,
    'format': 'json',
    # internal
    'https': True,
    'http_timeout': 30,
    'raw': False,
}

def make_requests_session():
    """
    :returns: requests session
    :rtype: :class:`requests.Session`
    """
    session = requests.Session()

    version = __import__('steam').__version__
    ua = "python-steam/{} {}".format(version,
                                session.headers['User-Agent'])
    session.headers['User-Agent'] = ua

    return session

def generate_session_id():
    """
    :returns: session id
    :rtype: :class:`str`
    """
    return hexlify(sha1_hash(random_bytes(32)))[:32].decode('ascii')
