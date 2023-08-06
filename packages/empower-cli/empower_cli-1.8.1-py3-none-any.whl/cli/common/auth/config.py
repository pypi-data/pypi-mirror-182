from pathlib import Path

HOST_NAME = "localhost"
PORT = 8080

REDIRECT_URI = f"http://{HOST_NAME}:{PORT}/sso-callback"

BROWSER_LOGIN_URL = (
    "$domain/auth/realms/$realm/protocol/openid-connect/auth?"
    f"response_type=code&client_id=$client_id&redirect_uri={REDIRECT_URI}"
)

CREDENTIALS_FILE_PATH = Path(Path.home() / ".empowercli/")
CREDENTIALS_FILE_PATH.mkdir(parents=True, exist_ok=True)

BROWSER_FLOW_CREDENTIALS_FILE = "access_token.json"
# TODO using the same file for all flows. Remove if no issues found
PIPELINE_FLOW_CREDENTIALS_FILE = BROWSER_FLOW_CREDENTIALS_FILE
# PIPELINE_FLOW_CREDENTIALS_FILE = "credentials.json"

HTML_TEMPLATES_PATH = Path(__file__).parent.resolve() / "templates"
SUCCESS_TEMPLATE_PATH = HTML_TEMPLATES_PATH / "success.html"
ERROR_TEMPLATE_PATH = HTML_TEMPLATES_PATH / "error.html"

# Keycloack/Credentials config
ACCESS_TOKEN_EXP_TIMEDELTA = 6 * 60 * 60
