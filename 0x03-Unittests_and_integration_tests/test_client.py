#!/usr/bin/env python3
"""Client module for interacting with the GitHub API"""

from typing import List, Dict
from functools import lru_cache
import requests

from utils import get_json


class GithubOrgClient:
    """GithubOrgClient class for fetching GitHub organization data"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name: str) -> None:
        """Initialize with organization name"""
        self.org_name = org_name

    @property
    @lru_cache()
    def org(self) -> Dict:
        """Return the organization data"""
        return get_json(self.ORG_URL.format(self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the repos_url from the organization data"""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Return the list of public repo names, optionally filtered by license"""
        repos = get_json(self._public_repos_url)
        repo_names = [
            repo["name"]
            for repo in repos
            if license is None or self.has_license(repo, license)
        ]
        return repo_names

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if a repository has a specific license"""
        license_info = repo.get("license")
        if license_info is None:
            return False
        return license_info.get("key") == license_key
