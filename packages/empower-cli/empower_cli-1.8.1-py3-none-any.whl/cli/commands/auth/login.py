import requests
import typer
from cli.common.auth import AuthAPIClient, credentials_flow_auth, browse, get_auth_uri
from cli.common.service_type import ServiceType
from cli.common.validation import validate_domain
from cli.common.schemas import OauthDomain
from typer import Argument
from cli.common.store_client import store
from cli.commands.empower_discovery.enterprise import EnterpriseCRUD

app = typer.Typer()
ENDPOINT = "auth"
SERVICE_TYPE = ServiceType.EMPOWER_AUTH


def get_api_response(domain) -> dict:
    api_client = AuthAPIClient(domain)
    return api_client.get_domain_auth_url()


def set_api_responses_to_store(domain_auth_url_response):
    oauth_domain = OauthDomain(**domain_auth_url_response)
    store.save("auth", **oauth_domain.dict())


def print_oauth_discovery_data():
    typer.echo(EnterpriseCRUD().get_oauth_domain())


@app.command(help="Login user within an opened browser tab.")
def login(domain: str = Argument(..., callback=validate_domain)) -> None:
    typer.echo("Processing login. Wait for the browser window to open.")

    domain_auth_url_response = get_api_response(domain)
    auth_url = get_auth_uri(domain_auth_url_response)

    try:
        browse(auth_url)
        typer.echo("Logged in successfully.")
        set_api_responses_to_store(domain_auth_url_response)
        typer.echo(f"Fetching discovery data from {domain}")
        print_oauth_discovery_data()
    except RuntimeError as e:
        typer.echo(e)
    except Exception as e:
        typer.echo(f"Authentication error: {e}")


@app.command(help="Pipeline authentication using 'client_credentials' flow.")
def login_pipeline() -> None:
    typer.echo("Processing login.")
    try:
        credentials_flow_auth()
        typer.echo("Logged in successfully.")
        typer.echo(f"Fetching discovery data")
        print_oauth_discovery_data()
    except requests.HTTPError:
        typer.echo("Error occurred while getting authentication credentials.")
        typer.Abort(1)
