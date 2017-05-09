# coding: utf-8

"""
    Broad probabilistic graphical models translator

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.1
    Contact: translator@broadinstitute.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class EvaluateModelModelInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, variable_group_id=None, model_variable=None):
        """
        EvaluateModelModelInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'variable_group_id': 'str',
            'model_variable': 'list[EvaluateModelModelVariable]'
        }

        self.attribute_map = {
            'variable_group_id': 'variableGroupId',
            'model_variable': 'modelVariable'
        }

        self._variable_group_id = variable_group_id
        self._model_variable = model_variable


    @property
    def variable_group_id(self):
        """
        Gets the variable_group_id of this EvaluateModelModelInput.


        :return: The variable_group_id of this EvaluateModelModelInput.
        :rtype: str
        """
        return self._variable_group_id

    @variable_group_id.setter
    def variable_group_id(self, variable_group_id):
        """
        Sets the variable_group_id of this EvaluateModelModelInput.


        :param variable_group_id: The variable_group_id of this EvaluateModelModelInput.
        :type: str
        """

        self._variable_group_id = variable_group_id

    @property
    def model_variable(self):
        """
        Gets the model_variable of this EvaluateModelModelInput.


        :return: The model_variable of this EvaluateModelModelInput.
        :rtype: list[EvaluateModelModelVariable]
        """
        return self._model_variable

    @model_variable.setter
    def model_variable(self, model_variable):
        """
        Sets the model_variable of this EvaluateModelModelInput.


        :param model_variable: The model_variable of this EvaluateModelModelInput.
        :type: list[EvaluateModelModelVariable]
        """

        self._model_variable = model_variable

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
