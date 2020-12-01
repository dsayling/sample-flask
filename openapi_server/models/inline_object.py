# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_name=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI

        :param file_name: The file_name of this InlineObject.  # noqa: E501
        :type file_name: file
        """
        self.openapi_types = {"file_name": file}

        self.attribute_map = {"file_name": "fileName"}

        self._file_name = file_name

    @classmethod
    def from_dict(cls, dikt) -> "InlineObject":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object of this InlineObject.  # noqa: E501
        :rtype: InlineObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_name(self):
        """Gets the file_name of this InlineObject.


        :return: The file_name of this InlineObject.
        :rtype: file
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this InlineObject.


        :param file_name: The file_name of this InlineObject.
        :type file_name: file
        """

        self._file_name = file_name
