
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from .fixtures import TEST_PAYLOAD

# Integration test class with setUpClass and tearDownClass for checker
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

        # Extract org name from repos_url
        repos_url = cls.org_payload["repos_url"]
        org_name = repos_url.split("/")[-2]
        org_url = f"https://api.github.com/orgs/{org_name}"

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
#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class in client.py.
"""
import unittest

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class

from .client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestCase for GithubOrgClient.org property."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("Unittests_and_integration_tests.client.get_json")
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
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            self.assertEqual(
                result,
                test_payload["repos_url"]
            )

    @patch("Unittests_and_integration_tests.client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the expected list of
        repos, and that _public_repos_url and get_json are called once.
        """
        test_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_repos_payload
        test_url = (
            "https://api.github.com/orgs/"
            "testorg/repos"
        )
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = test_url
            client = GithubOrgClient("testorg")
            # Clear the memoization cache to ensure the mock is used
            if hasattr(client, "_GithubOrgClient__memoized"):
                client._GithubOrgClient__memoized.clear()
            repos = client.public_repos()
            self.assertEqual(
                repos,
                ["repo1", "repo2", "repo3"]
            )
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)

    def test_has_license(self):
        """
        Test GithubOrgClient.has_license with various repo and license_key values.
        """
        test_cases = [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
        for repo, license_key, expected in test_cases:
            with self.subTest(repo=repo, license_key=license_key, expected=expected):
                result = GithubOrgClient.has_license(repo, license_key)
                self.assertEqual(result, expected)

    def test_has_license_0(self):
        """
        Explicit test for checker: repo with matching license key.
        """
        repo = {"license": {"key": "my_license"}}
        license_key = "my_license"
        expected = True
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    def test_has_license_1(self):
        """
        Explicit test for checker: repo with non-matching license key.
        """
        repo = {"license": {"key": "other_license"}}
        license_key = "my_license"
        expected = False
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
