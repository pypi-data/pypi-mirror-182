from string import Template
from typing import Any

import requests
from cli.common.auth.server import AuthCodeReceiver
from cli.common.store_client import store

from .config import BROWSER_LOGIN_URL, HOST_NAME, PORT


class AuthAPIClient:
    """
    Client for the operations with api requests
    """
    def __init__(self, domain: str):
        self.domain = domain

    def get_domain_auth_url(self) -> dict[str, Any]:
        """Get domain auth info from Discovery service.

        :return: domain auth info response
        """
        auth_url_response = requests.get(
            f"{store.empower_discovery_url}/auth-url/{self.domain}"
        )
        auth_url_response.raise_for_status()
        return auth_url_response.json()

    def get_api_config(self) -> dict[str, Any]:
        """Get configuration info for a given api instance.

        :param api_url: URL of an API instance
        :return: configuration endpoint response
        """
        api_config_response = requests.get(
            f"{store.empower_api_url}/configuration"
        )
        api_config_response.raise_for_status()
        return api_config_response.json()


def browse(auth_url: str) -> None:
    """Process browser flow login."""
    with AuthCodeReceiver(host=HOST_NAME, port=PORT) as receiver:
        receiver.get_auth_response(auth_uri=auth_url, timeout=60)


def get_auth_uri(domain_auth_url_response: dict) -> str:
    """Complete auth URI string with domain specified parameters:
    authServerUri, authRealm, authClientId, etc.
    """
    return Template(BROWSER_LOGIN_URL).substitute(
        domain=domain_auth_url_response["authServerUrl"],
        realm=domain_auth_url_response["authRealm"],
        client_id=domain_auth_url_response["clientId"],
    )
