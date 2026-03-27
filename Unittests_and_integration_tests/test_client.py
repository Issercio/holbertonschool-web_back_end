#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class in client.py.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestCase for GithubOrgClient.org property."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value and
        get_json is called once with the expected argument.
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        expected_payload = {"login": org_name, "id": 123}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL
        based on the mocked org payload.
        """
        test_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        with patch.object(GithubOrgClient, "org", new_callable=property) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])


    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the expected list of repos,
        and that _public_repos_url and get_json are called once.
        """
        test_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_repos_payload
        test_url = "https://api.github.com/orgs/testorg/repos"
        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=property) as mock_url:
            mock_url.return_value = test_url
            client = GithubOrgClient("testorg")
            # Clear the memoization cache to ensure the mock is used
            if hasattr(client, "_GithubOrgClient__memoized"):  # for memoize decorator
                client._GithubOrgClient__memoized.clear()
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
