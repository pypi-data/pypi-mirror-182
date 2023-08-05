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

from pulpcore.client.pulp_maven.configuration import Configuration


class MavenMavenDistribution(object):
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
        'base_path': 'str',
        'content_guard': 'str',
        'pulp_labels': 'dict(str, str)',
        'name': 'str',
        'repository': 'str',
        'remote': 'str'
    }

    attribute_map = {
        'base_path': 'base_path',
        'content_guard': 'content_guard',
        'pulp_labels': 'pulp_labels',
        'name': 'name',
        'repository': 'repository',
        'remote': 'remote'
    }

    def __init__(self, base_path=None, content_guard=None, pulp_labels=None, name=None, repository=None, remote=None, local_vars_configuration=None):  # noqa: E501
        """MavenMavenDistribution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_path = None
        self._content_guard = None
        self._pulp_labels = None
        self._name = None
        self._repository = None
        self._remote = None
        self.discriminator = None

        self.base_path = base_path
        self.content_guard = content_guard
        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        self.name = name
        self.repository = repository
        self.remote = remote

    @property
    def base_path(self):
        """Gets the base_path of this MavenMavenDistribution.  # noqa: E501

        The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")  # noqa: E501

        :return: The base_path of this MavenMavenDistribution.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this MavenMavenDistribution.

        The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")  # noqa: E501

        :param base_path: The base_path of this MavenMavenDistribution.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_path is None:  # noqa: E501
            raise ValueError("Invalid value for `base_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                base_path is not None and len(base_path) < 1):
            raise ValueError("Invalid value for `base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._base_path = base_path

    @property
    def content_guard(self):
        """Gets the content_guard of this MavenMavenDistribution.  # noqa: E501

        An optional content-guard.  # noqa: E501

        :return: The content_guard of this MavenMavenDistribution.  # noqa: E501
        :rtype: str
        """
        return self._content_guard

    @content_guard.setter
    def content_guard(self, content_guard):
        """Sets the content_guard of this MavenMavenDistribution.

        An optional content-guard.  # noqa: E501

        :param content_guard: The content_guard of this MavenMavenDistribution.  # noqa: E501
        :type: str
        """

        self._content_guard = content_guard

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this MavenMavenDistribution.  # noqa: E501


        :return: The pulp_labels of this MavenMavenDistribution.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this MavenMavenDistribution.


        :param pulp_labels: The pulp_labels of this MavenMavenDistribution.  # noqa: E501
        :type: dict(str, str)
        """

        self._pulp_labels = pulp_labels

    @property
    def name(self):
        """Gets the name of this MavenMavenDistribution.  # noqa: E501

        A unique name. Ex, `rawhide` and `stable`.  # noqa: E501

        :return: The name of this MavenMavenDistribution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MavenMavenDistribution.

        A unique name. Ex, `rawhide` and `stable`.  # noqa: E501

        :param name: The name of this MavenMavenDistribution.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def repository(self):
        """Gets the repository of this MavenMavenDistribution.  # noqa: E501

        The latest RepositoryVersion for this Repository will be served.  # noqa: E501

        :return: The repository of this MavenMavenDistribution.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this MavenMavenDistribution.

        The latest RepositoryVersion for this Repository will be served.  # noqa: E501

        :param repository: The repository of this MavenMavenDistribution.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def remote(self):
        """Gets the remote of this MavenMavenDistribution.  # noqa: E501

        Remote that can be used to fetch content when using pull-through caching.  # noqa: E501

        :return: The remote of this MavenMavenDistribution.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this MavenMavenDistribution.

        Remote that can be used to fetch content when using pull-through caching.  # noqa: E501

        :param remote: The remote of this MavenMavenDistribution.  # noqa: E501
        :type: str
        """

        self._remote = remote

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
        if not isinstance(other, MavenMavenDistribution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MavenMavenDistribution):
            return True

        return self.to_dict() != other.to_dict()
