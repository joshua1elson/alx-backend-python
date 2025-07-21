#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_payload, mock_get_json):
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test _public_repos_url returns correct repos_url from org"""
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test/repos"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")





@patch("client.get_json")
def test_public_repos(self, mock_get_json):
    """Test public_repos returns expected repo names"""
    mock_get_json.return_value = [
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ]

    with patch.object(
        GithubOrgClient,
        "_public_repos_url",
        return_value="https://api.github.com/orgs/test/repos"
    ) as mock_url:
        client = GithubOrgClient("test")
        repos = client.public_repos()

        self.assertEqual(repos, ["repo1", "repo2", "repo3"])
        mock_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test/repos"
        )
