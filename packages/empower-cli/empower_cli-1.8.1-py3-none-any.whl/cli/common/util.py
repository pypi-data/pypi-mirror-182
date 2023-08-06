import json
import pathlib
from io import TextIOWrapper
from typing import Optional

import typer
import yaml
from cli.common.service_type import ServiceType
from cli.common.store_client import store, StoreContainers


def get_json_data(value: Optional[TextIOWrapper]) -> Optional[str]:
    """Read input file.

    :param value: opened file object
    :raises typer.BadParameter: invalid file extension
    :return: file string data
    """
    if value is None:
        return
    if pathlib.Path(value.name).suffix != ".json":
        raise typer.BadParameter("Invalid file extension. Only '.json' files accepted.")
    return value.read()


def read_yaml_file(file_path: str) -> Optional[dict]:
    """Read input yaml file.

    :param file_path: file path
    :raises typer.BadParameter: invalid file extension
    :return: file string data
    """
    if file_path is None:
        return
    if pathlib.Path(file_path).suffix != ".yaml":
        raise typer.BadParameter("Invalid file extension. Only '.yaml' files accepted.")
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def import_local_json(file_path: str) -> dict:
    """Read JSON file data by its path.

    :param file_path: path to the JSON file.
    :raises typer.BadParameter: invalid file path
    :raises typer.BadParameter: file upload error
    :return: loaded JSON file data
    """
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise typer.BadParameter(
                f"An error occurred while uploading the file: '{file_path}'"
            ) from e


def get_request_url(service_type: ServiceType) -> str:
    """Get a URL for the request.

    :param service_type: service type string
    :return: request URL string
    """
    auth = store.get_all(StoreContainers.auth)
    strategy = {
        ServiceType.EMPOWER_DISCOVERY: store.empower_discovery_url,
        ServiceType.EMPOWER_API: store.empower_api_url,
        ServiceType.USER_SERVICE: auth["user_service_url"],
        ServiceType.SOURCE_TYPE: "http://localhost:8000",
    }
    return strategy[service_type]
