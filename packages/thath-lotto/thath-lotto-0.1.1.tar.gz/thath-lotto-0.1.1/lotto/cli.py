import argparse

from .main import main


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        "lotto", description="This is a simple lottery program", add_help=True
    )

    parser.add_argument(
        "-j", "--json", dest="json", action="store_true", help="Return results as JSON"
    )

    return parser


def cli():
    parser = get_parser()
    args = parser.parse_args()

    display_type = "json" if args.json else "txt"

    main(display_type)


if __name__ == "__main__":
    cli()
