# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBlackWhiteListsUsingGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'list_type': 'int',
        'address_type': 'int',
        'address': 'str',
        'port': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'list_type': 'list_type',
        'address_type': 'address_type',
        'address': 'address',
        'port': 'port',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, object_id=None, list_type=None, address_type=None, address=None, port=None, limit=None, offset=None):
        """ListBlackWhiteListsUsingGetRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id
        :type object_id: str
        :param list_type: 黑白名单类型4：黑名单，5：白名单
        :type list_type: int
        :param address_type: IP地址类型0：ipv4,1:ipv6,2:domain
        :type address_type: int
        :param address: ip地址
        :type address: str
        :param port: 端口
        :type port: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._object_id = None
        self._list_type = None
        self._address_type = None
        self._address = None
        self._port = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.object_id = object_id
        self.list_type = list_type
        if address_type is not None:
            self.address_type = address_type
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        self.limit = limit
        self.offset = offset

    @property
    def object_id(self):
        """Gets the object_id of this ListBlackWhiteListsUsingGetRequest.

        防护对象id

        :return: The object_id of this ListBlackWhiteListsUsingGetRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ListBlackWhiteListsUsingGetRequest.

        防护对象id

        :param object_id: The object_id of this ListBlackWhiteListsUsingGetRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def list_type(self):
        """Gets the list_type of this ListBlackWhiteListsUsingGetRequest.

        黑白名单类型4：黑名单，5：白名单

        :return: The list_type of this ListBlackWhiteListsUsingGetRequest.
        :rtype: int
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        """Sets the list_type of this ListBlackWhiteListsUsingGetRequest.

        黑白名单类型4：黑名单，5：白名单

        :param list_type: The list_type of this ListBlackWhiteListsUsingGetRequest.
        :type list_type: int
        """
        self._list_type = list_type

    @property
    def address_type(self):
        """Gets the address_type of this ListBlackWhiteListsUsingGetRequest.

        IP地址类型0：ipv4,1:ipv6,2:domain

        :return: The address_type of this ListBlackWhiteListsUsingGetRequest.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this ListBlackWhiteListsUsingGetRequest.

        IP地址类型0：ipv4,1:ipv6,2:domain

        :param address_type: The address_type of this ListBlackWhiteListsUsingGetRequest.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        """Gets the address of this ListBlackWhiteListsUsingGetRequest.

        ip地址

        :return: The address of this ListBlackWhiteListsUsingGetRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListBlackWhiteListsUsingGetRequest.

        ip地址

        :param address: The address of this ListBlackWhiteListsUsingGetRequest.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        """Gets the port of this ListBlackWhiteListsUsingGetRequest.

        端口

        :return: The port of this ListBlackWhiteListsUsingGetRequest.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListBlackWhiteListsUsingGetRequest.

        端口

        :param port: The port of this ListBlackWhiteListsUsingGetRequest.
        :type port: str
        """
        self._port = port

    @property
    def limit(self):
        """Gets the limit of this ListBlackWhiteListsUsingGetRequest.

        每页显示个数

        :return: The limit of this ListBlackWhiteListsUsingGetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBlackWhiteListsUsingGetRequest.

        每页显示个数

        :param limit: The limit of this ListBlackWhiteListsUsingGetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListBlackWhiteListsUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListBlackWhiteListsUsingGetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBlackWhiteListsUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListBlackWhiteListsUsingGetRequest.
        :type offset: int
        """
        self._offset = offset

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListBlackWhiteListsUsingGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
