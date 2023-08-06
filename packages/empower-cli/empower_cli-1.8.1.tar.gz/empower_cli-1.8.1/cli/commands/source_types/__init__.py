from cli.commands.source_types import execution_contexts, source_types

source_types_typer = source_types.app
source_types_typer.add_typer(execution_contexts.app, name="execution-context")
