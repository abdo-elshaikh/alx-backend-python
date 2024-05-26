#!/usr/bin/env python3
'''test utils module'''

import utils
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    '''test access nested map class'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, params, expected, expected_result):
        '''test access nested map'''
        self.assertEqual(
            utils.access_nested_map(params, expected), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, params, expected):
        '''test access nested map exception'''
        with self.assertRaises(KeyError):
            utils.access_nested_map(params, expected)


class TestGetJson(unittest.TestCase):
    '''test get json class'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = utils.get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
        mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    '''test memoize class'''

    def test_memoize(self):
        '''Test that memoize correctly caches the result of a method.'''
        class TestClass:
            '''test class'''
            def a_method(self):
                '''method'''
                return 42

            @memoize
            def a_property(self):
                '''a prp'''
                return self.a_method()

        obj = TestClass()
        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42) as mocked_method:
            result1 = obj.a_property()
            result2 = obj.a_property()
            mocked_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
