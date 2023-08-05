# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_deb.configuration import Configuration


class Repair(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'verify_checksums': 'bool'
    }

    attribute_map = {
        'verify_checksums': 'verify_checksums'
    }

    def __init__(self, verify_checksums=True, local_vars_configuration=None):  # noqa: E501
        """Repair - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._verify_checksums = None
        self.discriminator = None

        if verify_checksums is not None:
            self.verify_checksums = verify_checksums

    @property
    def verify_checksums(self):
        """Gets the verify_checksums of this Repair.  # noqa: E501

        Will verify that the checksum of all stored files matches what saved in the database. Otherwise only the existence of the files will be checked. Enabled by default  # noqa: E501

        :return: The verify_checksums of this Repair.  # noqa: E501
        :rtype: bool
        """
        return self._verify_checksums

    @verify_checksums.setter
    def verify_checksums(self, verify_checksums):
        """Sets the verify_checksums of this Repair.

        Will verify that the checksum of all stored files matches what saved in the database. Otherwise only the existence of the files will be checked. Enabled by default  # noqa: E501

        :param verify_checksums: The verify_checksums of this Repair.  # noqa: E501
        :type: bool
        """

        self._verify_checksums = verify_checksums

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Repair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Repair):
            return True

        return self.to_dict() != other.to_dict()
