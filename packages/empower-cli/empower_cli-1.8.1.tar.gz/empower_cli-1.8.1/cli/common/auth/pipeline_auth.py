import os

import requests
from cli.common.file_utils import write_credentials_to_json
from cli.common.store_client import store, StoreContainers

from .config import PIPELINE_FLOW_CREDENTIALS_FILE


def credentials_flow_auth(
    file_name: str = PIPELINE_FLOW_CREDENTIALS_FILE,
) -> None:
    """
    Get keycloak client credentials.

    :param file_name: credentials storage file name
    :return: keycloak client credentials json
    """
    auth = store.get_all(StoreContainers.auth)
    params = {
        "client_id": os.environ["EMPOWER_CLI_CLIENT_ID"],
        "client_secret": os.environ["EMPOWER_CLI_CLIENT_SECRET"],
        "grant_type": "client_credentials",
    }

    TOKEN_REQUEST_URL = f"{auth['server_url']}/auth/realms/{auth['realm']}/protocol/openid-connect/token"

    response = requests.post(TOKEN_REQUEST_URL, data=params)
    response.raise_for_status()
    credentials = response.json()
    write_credentials_to_json(credentials, file_name)
