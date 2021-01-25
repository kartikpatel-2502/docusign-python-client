# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ExternalClaim(object):
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
        'acquired_time': 'str',
        'claim_name': 'str',
        'provider': 'str',
        'value': 'str'
    }

    attribute_map = {
        'acquired_time': 'acquiredTime',
        'claim_name': 'claimName',
        'provider': 'provider',
        'value': 'value'
    }

    def __init__(self, acquired_time=None, claim_name=None, provider=None, value=None):  # noqa: E501
        """ExternalClaim - a model defined in Swagger"""  # noqa: E501

        self._acquired_time = None
        self._claim_name = None
        self._provider = None
        self._value = None
        self.discriminator = None

        if acquired_time is not None:
            self.acquired_time = acquired_time
        if claim_name is not None:
            self.claim_name = claim_name
        if provider is not None:
            self.provider = provider
        if value is not None:
            self.value = value

    @property
    def acquired_time(self):
        """Gets the acquired_time of this ExternalClaim.  # noqa: E501

          # noqa: E501

        :return: The acquired_time of this ExternalClaim.  # noqa: E501
        :rtype: str
        """
        return self._acquired_time

    @acquired_time.setter
    def acquired_time(self, acquired_time):
        """Sets the acquired_time of this ExternalClaim.

          # noqa: E501

        :param acquired_time: The acquired_time of this ExternalClaim.  # noqa: E501
        :type: str
        """

        self._acquired_time = acquired_time

    @property
    def claim_name(self):
        """Gets the claim_name of this ExternalClaim.  # noqa: E501

          # noqa: E501

        :return: The claim_name of this ExternalClaim.  # noqa: E501
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """Sets the claim_name of this ExternalClaim.

          # noqa: E501

        :param claim_name: The claim_name of this ExternalClaim.  # noqa: E501
        :type: str
        """

        self._claim_name = claim_name

    @property
    def provider(self):
        """Gets the provider of this ExternalClaim.  # noqa: E501

          # noqa: E501

        :return: The provider of this ExternalClaim.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ExternalClaim.

          # noqa: E501

        :param provider: The provider of this ExternalClaim.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def value(self):
        """Gets the value of this ExternalClaim.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this ExternalClaim.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExternalClaim.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this ExternalClaim.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(ExternalClaim, dict):
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
        if not isinstance(other, ExternalClaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other