import requests

from flask_apispec.views import MethodResource
from flask_restful import Resource


# pylint: disable=E0102
class Resource(MethodResource, Resource):
    pass

def update_object_from_dict(obj, data):
    """
    Update an object from a dictionary.

    :param obj: The object to update.
    :param data: The dictionary to update the object from.
    :return: The updated object.
    """
    for key in data:
        setattr(obj, key, data[key])
    return obj


def get_json(url):
    """
    Get the JSON response from a URL.

    :param url: The URL to get the JSON response from.
    :return: The JSON response.
    """
    response = requests.get(url)
    return response.json()


def get_json_from_ipfs(ipfs_hash):
    """
    Get the JSON response from an IPFS hash.

    :param ipfs_hash: The IPFS hash to get the JSON response from.
    :return: The JSON response.
    """
    try:
        if ipfs_hash.startswith("ipfs://"):
            ipfs_hash = ipfs_hash[7:]
        return get_json(f"https://ipfs.io/ipfs/{ipfs_hash}")
    except Exception:
        return {
            "url": ipfs_hash
        }

    

