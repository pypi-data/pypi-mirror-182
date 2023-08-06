import json
from typing import Optional

import typer
from cli.common.command_help import CRUD_FILE_PATH_HELP
from cli.common.command_util import handle_request_command
from cli.common.crud_command_base import CRUDCommandBase
from cli.common.enums import RequestMethods
from cli.common.service_type import ServiceType
from cli.common.util import get_json_data

app = typer.Typer()


class ConfigPromotionCRUD(CRUDCommandBase):
    def __init__(
        self,
        service_type: ServiceType = ServiceType.EMPOWER_API,
        endpoint: str = "config-promotion",
    ) -> None:
        super().__init__(service_type, endpoint)

    def config(self, data, endpoint):
        self._guard_input(data)
        url = self.default_url(endpoint)
        self._make_request(RequestMethods.POST, url, json=json.loads(data))

    def run(self, data):
        self._guard_input(data)
        url = self.default_url(self.endpoint)
        self._make_request(RequestMethods.POST, url, json=json.loads(data))

    def dump(self, endpoint):
        url = self.default_url(endpoint)
        self._make_request(RequestMethods.POST, url)

    def complete(self):
        url = self.default_url(self.endpoint)
        self._make_request(RequestMethods.PUT, url)

    def init(self, endpoint, data):
        self._guard_input(data)
        url = self.default_url(endpoint)
        self._make_request(RequestMethods.POST, url, json=json.loads(data))


@app.command(
    short_help="Configure current environment settings for Azure DevOps integration."
)
@handle_request_command
def configure_ado(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
):
    ConfigPromotionCRUD().config(
        json_ or file_path, endpoint="config-promotion/configure-azure-devops"
    )
    typer.echo("Azure DevOps integrations settings applied.")


@app.command(
    short_help="Configure current environment settings for GitHub integration."
)
@handle_request_command
def configure_git(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
):
    ConfigPromotionCRUD().config(
        json_ or file_path, endpoint="config-promotion/configure-git"
    )
    typer.echo("GitHub integration settings applied.")


@app.command(
    short_help=(
        "Create branches for each environment "
        "using 'dv' environment branch as HEAD (parent)."
    )
)
@handle_request_command
def init(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
):
    ConfigPromotionCRUD().init(
        "config-promotion/init-environments",
        json_ or file_path,
    )
    typer.echo("Environments initialized.")


@app.command(
    short_help="Dump promotable entities data from database to configured repository."
)
@handle_request_command
def dump():
    ConfigPromotionCRUD().dump(
        "config-promotion/dump",
    )
    typer.echo("Source environment data has been dumped.")


@app.command(
    short_help="Start promoting all promotable entities (creates PR in repository)."
)
@handle_request_command
def run(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
):
    ConfigPromotionCRUD().run(json_ or file_path)
    typer.echo("Configuration promotion started.")


@app.command(
    short_help=(
        "Complete promoting all promotable entities and apply all "
        "promoted to target environment (completes PR in repository)."
    )
)
@handle_request_command
def complete():
    ConfigPromotionCRUD().complete()
    typer.echo("Configuration promotion completed.")
