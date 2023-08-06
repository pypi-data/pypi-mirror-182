import json
from typing import Optional

import typer
from cli.common.command_help import CRUD_FILE_PATH_HELP
from cli.common.command_util import handle_request_command
from cli.common.crud_command_base import CRUDCommandBase
from cli.common.enums import RequestMethods
from cli.common.service_type import ServiceType
from cli.common.util import get_json_data, get_request_url, read_yaml_file

ENDPOINT = "source-type"
app = typer.Typer()


class SourceTypeCRUD(CRUDCommandBase):
    def __init__(
        self,
        service_type: ServiceType = ServiceType.SOURCE_TYPE,
        endpoint: str = ENDPOINT,
    ) -> None:
        super().__init__(service_type, endpoint)

    def delete_img(self, source_type_name_):
        url = f"{get_request_url(self.service_type)}/{self.endpoint}/{source_type_name_}/images"
        self._make_request(RequestMethods.DELETE, url)
        typer.echo(
            f'Logo for {self.endpoint} object with name: "{source_type_name_}" successfully deleted'
        )

    def update_image(self, source_type_name, image_file_path):

        url = f"{get_request_url(self.service_type)}/{self.endpoint}/{source_type_name}/images"
        try:
            with open(image_file_path, "rb") as file:

                file_name, file_format = file.name.split(".")

                file_format = "image/svg+xml" if file_format == "svg" else f"image/{file_format}"

                updated = self._make_request(
                    RequestMethods.POST,
                    url,
                    files={"logo": (file_name, file, file_format)},
                ).json()
                return updated
        except FileNotFoundError:
            return typer.echo(f'Image file with path: "{image_file_path}" not found!')


@app.command("list", help="Get All Source Types")
@handle_request_command
def list_():
    typer.echo(SourceTypeCRUD().get())


@app.command("name", help="Get Source Type By SourceTypeName")
@handle_request_command
def get_source_type(
    source_type_name: str = typer.Argument(..., metavar="Source Type Name")
):
    typer.echo(SourceTypeCRUD().get_by_id(source_type_name))


@app.command("create", help="Create Source Type")
@handle_request_command
def create_source_type(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
    yaml_file: Optional[str] = typer.Option(None, "--yaml"),
):
    typer.echo(SourceTypeCRUD().create(json_ or file_path or read_yaml_file(yaml_file)))


@app.command("update", help="Update Source Type")
@handle_request_command
def update_source_type(
    source_type_name: str = typer.Argument(
        ...,
        metavar="Source Type Name",
    ),
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
    yaml_file: Optional[str] = typer.Option(None, "--yaml"),
):
    typer.echo(
        SourceTypeCRUD().update(
            data=json_ or file_path or read_yaml_file(yaml_file),
            endpoint=f"{ENDPOINT}/{source_type_name}",
        )
    )


@app.command("delete", help="Delete Source Type")
@handle_request_command
def delete_source_type(
    source_type_name: str = typer.Argument(
        ...,
        metavar="Source Type Name",
    )
):
    typer.echo(SourceTypeCRUD().delete(source_type_name))


@app.command("image-update", help="Update Source Type image")
@handle_request_command
def update_source_type_image(
    source_type_name: str = typer.Argument(..., metavar="Source Type Name"),
    image_file_path: str = typer.Argument(..., metavar="Path to image file"),
):
    typer.echo(SourceTypeCRUD().update_image(source_type_name, image_file_path))


@app.command("image-delete", help="Delete Source Type image")
@handle_request_command
def delete_source_type_image(
    source_type_name_: str = typer.Argument(..., metavar="Source Type Name"),
):
    typer.echo(SourceTypeCRUD().delete_img(source_type_name_))
