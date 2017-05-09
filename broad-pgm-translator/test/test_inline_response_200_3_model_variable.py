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

from __future__ import absolute_import

import os
import sys
import unittest

import broad_pgm_translator
from broad_pgm_translator.rest import ApiException
from broad_pgm_translator.models.inline_response_200_3_model_variable import InlineResponse2003ModelVariable


class TestInlineResponse2003ModelVariable(unittest.TestCase):
    """ InlineResponse2003ModelVariable unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2003ModelVariable(self):
        """
        Test InlineResponse2003ModelVariable
        """
        model = broad_pgm_translator.models.inline_response_200_3_model_variable.InlineResponse2003ModelVariable()


if __name__ == '__main__':
    unittest.main()
