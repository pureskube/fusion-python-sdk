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

class Operation(object):
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
        'id': 'str',
        'self_link': 'str',
        'request': 'OperationRequest',
        'request_type': 'str',
        'request_id': 'str',
        'request_collection': 'str',
        'state': 'OperationState',
        'result': 'OperationResult',
        'status': 'str',
        'retry_in': 'int',
        'error': 'Error',
        'created_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'self_link': 'self_link',
        'request': 'request',
        'request_type': 'request_type',
        'request_id': 'request_id',
        'request_collection': 'request_collection',
        'state': 'state',
        'result': 'result',
        'status': 'status',
        'retry_in': 'retry_in',
        'error': 'error',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, self_link=None, request=None, request_type=None, request_id=None, request_collection=None, state=None, result=None, status=None, retry_in=None, error=None, created_at=None):  # noqa: E501
        """Operation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._self_link = None
        self._request = None
        self._request_type = None
        self._request_id = None
        self._request_collection = None
        self._state = None
        self._result = None
        self._status = None
        self._retry_in = None
        self._error = None
        self._created_at = None
        self.discriminator = None
        self.id = id
        self.self_link = self_link
        if request is not None:
            self.request = request
        self.request_type = request_type
        self.request_id = request_id
        if request_collection is not None:
            self.request_collection = request_collection
        if state is not None:
            self.state = state
        if result is not None:
            self.result = result
        self.status = status
        self.retry_in = retry_in
        if error is not None:
            self.error = error
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this Operation.  # noqa: E501

        The UUID of the operation.  # noqa: E501

        :return: The id of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Operation.

        The UUID of the operation.  # noqa: E501

        :param id: The id of this Operation.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def self_link(self):
        """Gets the self_link of this Operation.  # noqa: E501

        The URI of the operation, e.g., /tenants/<t>/tenant-spaces/<ts>/volumes/<v>.   # noqa: E501

        :return: The self_link of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """Sets the self_link of this Operation.

        The URI of the operation, e.g., /tenants/<t>/tenant-spaces/<ts>/volumes/<v>.   # noqa: E501

        :param self_link: The self_link of this Operation.  # noqa: E501
        :type: str
        """
        if self_link is None:
            raise ValueError("Invalid value for `self_link`, must not be `None`")  # noqa: E501

        self._self_link = self_link

    @property
    def request(self):
        """Gets the request of this Operation.  # noqa: E501


        :return: The request of this Operation.  # noqa: E501
        :rtype: OperationRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Operation.


        :param request: The request of this Operation.  # noqa: E501
        :type: OperationRequest
        """

        self._request = request

    @property
    def request_type(self):
        """Gets the request_type of this Operation.  # noqa: E501

        Request type is a combination of action and resource kind, e.g., \"CreateVolume\".  # noqa: E501

        :return: The request_type of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this Operation.

        Request type is a combination of action and resource kind, e.g., \"CreateVolume\".  # noqa: E501

        :param request_type: The request_type of this Operation.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = request_type

    @property
    def request_id(self):
        """Gets the request_id of this Operation.  # noqa: E501

        The request ID specified with the REST call (or system generated) used for idempotence when making API calls. Any name is valid.  # noqa: E501

        :return: The request_id of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Operation.

        The request ID specified with the REST call (or system generated) used for idempotence when making API calls. Any name is valid.  # noqa: E501

        :param request_id: The request_id of this Operation.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def request_collection(self):
        """Gets the request_collection of this Operation.  # noqa: E501

        The URI of the request collection in which this operation was created. Valid values are \"/\", \"/<tenants>/<t>\" or \"/<tenants>/<t>/tenant-spaces<ts>\".  # noqa: E501

        :return: The request_collection of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._request_collection

    @request_collection.setter
    def request_collection(self, request_collection):
        """Sets the request_collection of this Operation.

        The URI of the request collection in which this operation was created. Valid values are \"/\", \"/<tenants>/<t>\" or \"/<tenants>/<t>/tenant-spaces<ts>\".  # noqa: E501

        :param request_collection: The request_collection of this Operation.  # noqa: E501
        :type: str
        """

        self._request_collection = request_collection

    @property
    def state(self):
        """Gets the state of this Operation.  # noqa: E501


        :return: The state of this Operation.  # noqa: E501
        :rtype: OperationState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Operation.


        :param state: The state of this Operation.  # noqa: E501
        :type: OperationState
        """

        self._state = state

    @property
    def result(self):
        """Gets the result of this Operation.  # noqa: E501


        :return: The result of this Operation.  # noqa: E501
        :rtype: OperationResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Operation.


        :param result: The result of this Operation.  # noqa: E501
        :type: OperationResult
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this Operation.  # noqa: E501

        The latest status of the operation indicates if it is waiting (Pending), active (Running, Aborting) or complete (Succeeded, Failed).  # noqa: E501

        :return: The status of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Operation.

        The latest status of the operation indicates if it is waiting (Pending), active (Running, Aborting) or complete (Succeeded, Failed).  # noqa: E501

        :param status: The status of this Operation.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Pending", "Running", "Aborting", "Succeeded", "Failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def retry_in(self):
        """Gets the retry_in of this Operation.  # noqa: E501

        Recommended time to wait before getting the operation again to observe status change (polling interval). Unit is milliseconds, e.g., 100.  # noqa: E501

        :return: The retry_in of this Operation.  # noqa: E501
        :rtype: int
        """
        return self._retry_in

    @retry_in.setter
    def retry_in(self, retry_in):
        """Sets the retry_in of this Operation.

        Recommended time to wait before getting the operation again to observe status change (polling interval). Unit is milliseconds, e.g., 100.  # noqa: E501

        :param retry_in: The retry_in of this Operation.  # noqa: E501
        :type: int
        """
        if retry_in is None:
            raise ValueError("Invalid value for `retry_in`, must not be `None`")  # noqa: E501

        self._retry_in = retry_in

    @property
    def error(self):
        """Gets the error of this Operation.  # noqa: E501


        :return: The error of this Operation.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Operation.


        :param error: The error of this Operation.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def created_at(self):
        """Gets the created_at of this Operation.  # noqa: E501

        The time that the operation was created, in milliseconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this Operation.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Operation.

        The time that the operation was created, in milliseconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this Operation.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(Operation, dict):
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
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other