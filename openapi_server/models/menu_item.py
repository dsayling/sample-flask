# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MenuItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, description=None, name=None, price=None, image_id=None):  # noqa: E501
        """MenuItem - a model defined in OpenAPI

        :param id: The id of this MenuItem.  # noqa: E501
        :type id: int
        :param description: The description of this MenuItem.  # noqa: E501
        :type description: str
        :param name: The name of this MenuItem.  # noqa: E501
        :type name: str
        :param price: The price of this MenuItem.  # noqa: E501
        :type price: float
        :param image_id: The image_id of this MenuItem.  # noqa: E501
        :type image_id: int
        """
        self.openapi_types = {
            'id': int,
            'description': str,
            'name': str,
            'price': float,
            'image_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'name': 'name',
            'price': 'price',
            'image_id': 'imageId'
        }

        self._id = id
        self._description = description
        self._name = name
        self._price = price
        self._image_id = image_id

    @classmethod
    def from_dict(cls, dikt) -> 'MenuItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MenuItem of this MenuItem.  # noqa: E501
        :rtype: MenuItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this MenuItem.


        :return: The id of this MenuItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MenuItem.


        :param id: The id of this MenuItem.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this MenuItem.


        :return: The description of this MenuItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MenuItem.


        :param description: The description of this MenuItem.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this MenuItem.


        :return: The name of this MenuItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MenuItem.


        :param name: The name of this MenuItem.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this MenuItem.


        :return: The price of this MenuItem.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MenuItem.


        :param price: The price of this MenuItem.
        :type price: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def image_id(self):
        """Gets the image_id of this MenuItem.

        URL to an image of the menu item.  This should be the image from the /image endpoint   # noqa: E501

        :return: The image_id of this MenuItem.
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this MenuItem.

        URL to an image of the menu item.  This should be the image from the /image endpoint   # noqa: E501

        :param image_id: The image_id of this MenuItem.
        :type image_id: int
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id
