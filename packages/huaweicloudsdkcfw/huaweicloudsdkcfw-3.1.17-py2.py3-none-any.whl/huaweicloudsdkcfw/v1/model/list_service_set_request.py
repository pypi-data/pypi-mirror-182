# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceSetRequest:

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
        'key_word': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'key_word': 'key_word',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, object_id=None, key_word=None, limit=None, offset=None):
        """ListServiceSetRequest

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id
        :type object_id: str
        :param key_word: 关键字
        :type key_word: str
        :param limit: 每页查询个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._object_id = None
        self._key_word = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.object_id = object_id
        if key_word is not None:
            self.key_word = key_word
        self.limit = limit
        self.offset = offset

    @property
    def object_id(self):
        """Gets the object_id of this ListServiceSetRequest.

        防护对象id

        :return: The object_id of this ListServiceSetRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ListServiceSetRequest.

        防护对象id

        :param object_id: The object_id of this ListServiceSetRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def key_word(self):
        """Gets the key_word of this ListServiceSetRequest.

        关键字

        :return: The key_word of this ListServiceSetRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this ListServiceSetRequest.

        关键字

        :param key_word: The key_word of this ListServiceSetRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def limit(self):
        """Gets the limit of this ListServiceSetRequest.

        每页查询个数

        :return: The limit of this ListServiceSetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServiceSetRequest.

        每页查询个数

        :param limit: The limit of this ListServiceSetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServiceSetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListServiceSetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServiceSetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListServiceSetRequest.
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
        if not isinstance(other, ListServiceSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
