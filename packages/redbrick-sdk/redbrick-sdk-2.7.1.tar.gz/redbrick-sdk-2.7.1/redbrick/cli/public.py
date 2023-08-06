"""Main file for CLI."""
import sys
import argparse
from typing import Any, List, Optional

import redbrick
from redbrick.cli.command import (
    CLIConfigController,
    CLIInitController,
    CLICloneController,
    CLIInfoController,
    CLIExportController,
    CLIUploadController,
    CLIIReportController,
)
from redbrick.cli.cli_base import CLIInterface
from redbrick.utils.logging import logger


class CLIController(CLIInterface):
    """Main CLI Controller."""

    def __init__(self, command: argparse._SubParsersAction) -> None:
        """Initialize CLI command parsers."""
        self.config = CLIConfigController(
            command.add_parser(self.CONFIG, help="Setup credentials")
        )
        self.init = CLIInitController(
            command.add_parser(self.INIT, help="Create a new project")
        )
        self.clone = CLICloneController(
            command.add_parser(
                self.CLONE, help="Clone an existing remote project to local"
            )
        )
        self.info = CLIInfoController(
            command.add_parser(self.INFO, help="Get a project's information")
        )
        self.export = CLIExportController(
            command.add_parser(self.EXPORT, help="Export data for a project")
        )
        self.upload = CLIUploadController(
            command.add_parser(self.UPLOAD, help="Upload files to a project")
        )
        self.report = CLIIReportController(
            command.add_parser(self.REPORT, help="Generate report for a project")
        )

    def handle_command(self, args: argparse.Namespace) -> None:
        """CLI command main handler."""
        if args.command == self.CONFIG:
            self.config.handler(args)
        elif args.command == self.INIT:
            self.init.handler(args)
        elif args.command == self.CLONE:
            self.clone.handler(args)
        elif args.command == self.INFO:
            self.info.handler(args)
        elif args.command == self.EXPORT:
            self.export.handler(args)
        elif args.command == self.UPLOAD:
            self.upload.handler(args)
        elif args.command == self.REPORT:
            self.report.handler(args)
        else:
            raise argparse.ArgumentError(None, "")


def cli_parser(generate_docs: bool = True) -> Any:
    """Initialize argument parser."""
    parser = argparse.ArgumentParser(description="RedBrick AI")
    parser.add_argument(
        "-v", "--version", action="version", version=f"v{redbrick.__version__}"
    )
    cli = CLIController(parser.add_subparsers(title="Commands", dest="command"))

    if generate_docs:
        return parser

    return parser, cli


def cli_main(argv: Optional[List[str]] = None) -> None:
    """CLI main handler."""
    parser: argparse.ArgumentParser
    cli: CLIController

    parser, cli = cli_parser(False)

    try:
        args = parser.parse_args(argv if argv is not None else sys.argv[1:])
        logger.debug(args)
    except KeyboardInterrupt:
        logger.warning("User interrupted")
    except argparse.ArgumentError as error:
        logger.warning(str(error))
        parser.print_help()
    else:
        try:
            cli.handle_command(args)
        except KeyboardInterrupt:
            logger.warning("User interrupted")
        except argparse.ArgumentError:
            parser.print_usage()


if __name__ == "__main__":
    cli_main()
