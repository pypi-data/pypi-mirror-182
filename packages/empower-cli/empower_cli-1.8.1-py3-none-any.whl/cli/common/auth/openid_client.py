import json
import requests

from functools import cache
from keycloak import KeycloakOpenID
from cli.common.store_client import store, StoreContainers
from jwt.algorithms import RSAAlgorithm


def __get_secret_key(certs_url: str):
    certs: list = requests.get(certs_url).json()['keys']
    rs256: dict = [cert for cert in certs if cert["alg"] == "RS256"][0]
    return RSAAlgorithm.from_jwk(json.dumps(rs256))


@cache
def get_openid_client():
    auth = store.get_all(StoreContainers.auth)

    rsa_key = __get_secret_key(
        f"{auth['server_url']}/auth/realms/{auth['realm']}/protocol/openid-connect/certs"
    )

    return KeycloakOpenID(
        server_url=f"{auth['user_service_url']}/auth/",
        client_id=auth['client_id'],
        realm_name=auth['realm'],
        client_secret_key=rsa_key,
    )
