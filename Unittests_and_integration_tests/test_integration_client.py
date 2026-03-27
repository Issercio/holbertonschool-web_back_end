#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient.public_repos using fixtures.
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
from .client import GithubOrgClient
from .fixtures import TEST_PAYLOAD

@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
    for org_payload, repos_payload, expected_repos, apache2_repos in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get and set up side_effect."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        org_url = cls.org_payload["repos_url"].replace("/repos", "")
        repos_url = cls.org_payload["repos_url"]

        def side_effect(url):
            mock_resp = MagicMock()
            if url == org_url:
                mock_resp.json.return_value = cls.org_payload
            elif url == repos_url:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = None
            return mock_resp

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repo names."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos returns repos with apache2 license only."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)
