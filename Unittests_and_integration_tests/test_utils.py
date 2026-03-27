sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


#!/usr/bin/env python3
"""Unit tests for utils.py functions."""

import sys
import os
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, exc):
        with self.assertRaises(exc):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        with patch("utils.requests.get") as mock_get:
            mock_resp = Mock()
            mock_resp.json.return_value = payload
            mock_get.return_value = mock_resp
            self.assertEqual(get_json(url), payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize


            #!/usr/bin/env python3
            # Unit tests for utils.py functions
            import sys
            import os
            import unittest
            from parameterized import parameterized
            from unittest.mock import patch, Mock

            sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
            from utils import access_nested_map, get_json, memoize


            class TestAccessNestedMap(unittest.TestCase):

                @parameterized.expand([
                    ({'a': 1}, ('a',), 1),
                    ({'a': {'b': 2}}, ('a',), {'b': 2}),
                    ({'a': {'b': 2}}, ('a', 'b'), 2)
                ])
                def test_access_nested_map(self, nested_map, path, expected):
                    self.assertEqual(access_nested_map(nested_map, path), expected)

                @parameterized.expand([
                    ({}, ('a',), KeyError),
                    ({'a': 1}, ('a', 'b'), KeyError)
                ])
                def test_access_nested_map_exception(self, nested_map, path, exc):
                    with self.assertRaises(exc):
                        access_nested_map(nested_map, path)


            class TestGetJson(unittest.TestCase):

                @parameterized.expand([
                    ("http://example.com", {"payload": True}),
                    ("http://holberton.io", {"payload": False})
                ])
                def test_get_json(self, url, payload):
                    with patch("utils.requests.get") as mock_get:
                        mock_resp = Mock()
                        mock_resp.json.return_value = payload
                        mock_get.return_value = mock_resp
                        self.assertEqual(get_json(url), payload)
                        mock_get.assert_called_once_with(url)


            class TestMemoize(unittest.TestCase):

                def test_memoize(self):
                    class TestClass:
                        def a_method(self):
                            return 42

                        @memoize
                        def a_property(self):
                            return self.a_method()

                    with patch.object(TestClass, "a_method", return_value=42) as mock_method:
                        obj = TestClass()
                        self.assertEqual(obj.a_property, 42)
                        self.assertEqual(obj.a_property, 42)
                        mock_method.assert_called_once()
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


class TestGetJson(unittest.TestCase):
    """Test case for get_json function.
    This class tests that get_json returns the expected payload and does not
    make real HTTP calls.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ], name_func=lambda f, n, p: f"test_get_json_{n}")
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected payload and requests.get is
        called correctly.
        """
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function.
    This class tests that access_nested_map returns the expected value for
    various nested dictionaries and paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(
            access_nested_map(nested_map, path),
            expected
        )

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)
