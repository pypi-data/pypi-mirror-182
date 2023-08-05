import click

from . import __version__ as VERSION


@click.group()
@click.version_option(message="%(prog)s v%(version)s", version=VERSION)
def cli():
    """
    Test CLI.
    """


def main():
    cli()


if __name__ == '__main__':
    main()
