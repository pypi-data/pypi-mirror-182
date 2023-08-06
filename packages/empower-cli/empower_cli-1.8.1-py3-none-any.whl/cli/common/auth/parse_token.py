from cli.common.auth.openid_client import get_openid_client

def get_user_info(token: str) -> dict[str, str]:
    """Parse user info from access token.

    :param token: access token string
    :return: user info dictionary
    """
    keycloak_openid = get_openid_client()
    user_fields = ("sub", "name", "email", "preferred_username")
    return {
        key: value
        for key, value in keycloak_openid.userinfo(token).items()
        if key in user_fields
    }
