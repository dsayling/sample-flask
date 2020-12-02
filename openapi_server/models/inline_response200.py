# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image_id=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param image_id: The image_id of this InlineResponse200.  # noqa: E501
        :type image_id: int
        """
        self.openapi_types = {"image_id": int}

        self.attribute_map = {"image_id": "imageId"}

        self._image_id = image_id

    @classmethod
    def from_dict(cls, dikt) -> "InlineResponse200":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_id(self):
        """Gets the image_id of this InlineResponse200.


        :return: The image_id of this InlineResponse200.
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this InlineResponse200.


        :param image_id: The image_id of this InlineResponse200.
        :type image_id: int
        """

        self._image_id = image_id
