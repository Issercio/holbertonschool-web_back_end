

#!/usr/bin/env python3
# Unit tests for utils module.
# This module contains test cases for the access_nested_map function.
import unittest
from parameterized import parameterized
from .utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for access_nested_map utility function.
    This class contains parameterized tests for different nested map scenarios.
    """

    @parameterized.expand([
        ("{} and ('a',)", {}, ('a',), 'a'),
        ("{'a': 1} and ('a', 'b')", {'a': 1}, ('a', 'b'), 'b'),
    ])
    def test_access_nested_map_exception(self, name: str, nested_map: dict,
                                         path: tuple, expected_key: str) -> None:
        """Test access_nested_map raises KeyError with correct message.
        Args:
            name (str): Description of the test case.
            nested_map (dict): The nested dictionary to test.
            path (tuple): The path of keys to access.
            expected_key (str): The key expected in the KeyError message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'")

    @parameterized.expand([
        ("{'a': 1}, ('a',)", {'a': 1}, ('a',), 1),
        ("{'a': {'b': 2}}, ('a',)", {'a': {'b': 2}}, ('a',), {'b': 2}),
        ("{'a': {'b': 2}}, ('a', 'b')",
         {'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, name: str, nested_map: dict,
                               path: tuple, expected: object) -> None:
        """Test access_nested_map returns expected result for given path.
        Args:
            name (str): Description of the test case.
            nested_map (dict): The nested dictionary to test.
            path (tuple): The path of keys to access.
            expected (object): The expected value from the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

