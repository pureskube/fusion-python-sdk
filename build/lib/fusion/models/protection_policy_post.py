# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProtectionPolicyPost(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'display_name': 'str',
        'objectives': 'list[OneOfProtectionPolicyPostObjectivesItems]'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'objectives': 'objectives'
    }

    def __init__(self, name=None, display_name=None, objectives=None):  # noqa: E501
        """ProtectionPolicyPost - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._display_name = None
        self._objectives = None
        self.discriminator = None
        self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.objectives = objectives

    @property
    def name(self):
        """Gets the name of this ProtectionPolicyPost.  # noqa: E501

        The name of the resource, supplied by the user at creation, and used in the URI path of a resource.  # noqa: E501

        :return: The name of this ProtectionPolicyPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtectionPolicyPost.

        The name of the resource, supplied by the user at creation, and used in the URI path of a resource.  # noqa: E501

        :param name: The name of this ProtectionPolicyPost.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this ProtectionPolicyPost.  # noqa: E501

        The display name of the resource.  # noqa: E501

        :return: The display_name of this ProtectionPolicyPost.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ProtectionPolicyPost.

        The display name of the resource.  # noqa: E501

        :param display_name: The display_name of this ProtectionPolicyPost.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def objectives(self):
        """Gets the objectives of this ProtectionPolicyPost.  # noqa: E501

        A JSON array of objectives  # noqa: E501

        :return: The objectives of this ProtectionPolicyPost.  # noqa: E501
        :rtype: list[OneOfProtectionPolicyPostObjectivesItems]
        """
        return self._objectives

    @objectives.setter
    def objectives(self, objectives):
        """Sets the objectives of this ProtectionPolicyPost.

        A JSON array of objectives  # noqa: E501

        :param objectives: The objectives of this ProtectionPolicyPost.  # noqa: E501
        :type: list[OneOfProtectionPolicyPostObjectivesItems]
        """
        if objectives is None:
            raise ValueError("Invalid value for `objectives`, must not be `None`")  # noqa: E501

        self._objectives = objectives

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProtectionPolicyPost, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtectionPolicyPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other