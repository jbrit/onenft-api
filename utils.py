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