#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map"""
import unittest
from parameterized import parameterized
import sys
import os
import unittest
from parameterized import parameterized
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function. This class tests that access_nested_map returns the expected value for various nested dictionaries and paths."""

    @parameterized.expand([
        ( {"a": 1}, ("a",), 1),
        ( {"a": {"b": 2}}, ("a",), {"b": 2}),
        ( {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected value for a given path."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
